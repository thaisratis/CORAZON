def kMeans(fn1, genes, user, id, num_cluster, maxiter, attributes, nomeCol):
	
	from sklearn.cluster import KMeans
	import numpy as np
	import sys
	import mysql.connector
	import os
	import remove_files
	
	con = mysql.connector.connect(user='biodados', password= 'sacizeir0', host= 'db', database='meanshift')
	cursor=con.cursor()
	#print('chamou')
	
	if(attributes =="0"):
		#print('entrou no if')
		X = np.loadtxt(fn1, delimiter=';', dtype=bytes).astype(str)
		#arquivo = open(fn2, 'r')
		arquivosaida = open("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/result", 'w')

		table_name = "result_KMeans" + str(id)
		table= 'create table ' + table_name + '(ENSEMBL varchar(255), CLUSTER int, index ENS_idx(ENSEMBL));'
		cursor.execute(table)
		sys.stdout = open ("arquivo", "w")

		np.set_printoptions(threshold='nan')
		X= np.asarray(X, dtype=float)
					   
		kmeans = KMeans(n_clusters=num_cluster, random_state=0, max_iter = maxiter).fit(X)
		kmeans.labels_

		matriz= kmeans.fit_predict(X)

		kmeans.cluster_centers_
		
		newmatriz = []
		#genes=[]

		#for line in arquivo:
		#	genes.append(line.strip())
			
		arquivosaida.write("Number of clusters: " + str(num_cluster) + '\n')
		arquivosaida.write("Max Iteration: " + str(maxiter)+ '\n')

		for i in range(0,len(matriz)):
			#var= (str(genes[i]) + '\t' + str(matriz[i]))
			var= 'insert into ' + table_name + ' values("'+ str(genes[i])+'",'+str(matriz[i])+');'
			cursor.execute(var)
			arquivosaida.write(str(genes[i]) + '\t' + str(matriz[i])+ '\n')

		remove_table = 'drop table ' + table_name + ';'
		cursor.execute(remove_table)

			
	else:
		
		table_name = "result_KMeansSelectAttributes" + str(id)
		table= 'create table ' + table_name + '(ENSEMBL varchar(255), '
		dir = '/var/www/html/users/' + user + '/' + str(id) + '/Resultados/'		
		os.mkdir(dir)
		#print(nomeCol)
		#arquivosaida = open("/var/www/html/clustering/users/" + str(user)+ "/" + str(id)+ "/result", 'w')
		for x in range(1, len(nomeCol)-1):
			table += nomeCol[x] + ' varchar(255), '
		
		
		table+= nomeCol[len(nomeCol)-1] + ' varchar(255), index ENSEMBL_idx(ENSEMBL)); '
		
		droptable = "drop table if exists " + table_name + ";"
		cursor.execute(droptable) 
		cursor.execute(table)
		
			
		for x in range(0,len(genes)):
			var= 'insert into ' + table_name + ' (ENSEMBL) values("'+ str(genes[x])+ '");'
			cursor.execute(var)
		
		
		
		for y in range(1,len(nomeCol)):
			print('eliminando coluna: ' + str(nomeCol[y])+ '\n')
			cut = "cat " + fn1 + " | cut -d ';' -f "
			for i in range (1,len(nomeCol)):
				if(i != y):
					cut+= str(i+1) + ','
			cut = cut[:-1]
			
			saida = dir + 'result_' + user + '_' + str(id) + '_' + str(y)
			cutsaida = cut + ' > ' + saida
			print(cutsaida)
			os.system(cutsaida)
			
			saida2 = open(dir + 'result_' + str(nomeCol[y]), 'w')
			X = np.loadtxt(saida, delimiter=';', dtype=bytes).astype(str)
			
			np.set_printoptions(threshold='nan')
			X= np.asarray(X, dtype=float)
			
			kmeans = KMeans(n_clusters=num_cluster, random_state=0, max_iter = maxiter).fit(X)
			kmeans.labels_

			matriz= kmeans.fit_predict(X)

			kmeans.cluster_centers_
		

			newmatriz = []

		#	arquivosaida.write("Number of clusters: " +str(num_cluster))
		#	arquivosaida.write("Max Iteration: " + str(maxiter))			
			

			for i in range(0,len(matriz)):
				up = 'update ' + table_name + ' set ' + str(nomeCol[y]) + ' = ' + str(matriz[i])+ ' where ENSEMBL = "' + str(genes[i]) + '";'
				#print(up)
				cursor.execute(up)
				saida2.write(str(genes[i]) + '\t' + str(matriz[i])+ '\n')
		
		arquivototal = open('/var/www/html/users/' + user + '/' + str(id) + '/result', 'w')
		arquivototal.write("Number of clusters: " + str(num_cluster) + '\n')
		arquivototal.write("Max Iterarion: " + str(maxiter) + '\n')
		for line in nomeCol:
			arquivototal.write(line + '\t')

		arquivototal.write('\n')
		arquivototal.close()
		tabela = 'select * from ' + table_name + ' into outfile "/tmp/resultado";'
		cursor.execute(tabela)
		os.system('cat /tmp/resultado >> ' + '/var/www/html/users/' + user + '/' + str(id) + '/result')
		os.remove('/tmp/resultado')
		remove_table = 'drop table ' + table_name + ';'
		cursor.execute(remove_table)

#	remove_files.Remove_Files(user, id)




