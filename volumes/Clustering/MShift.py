def mshift(fn1, genes, user, id, bandwidth, cluster_all, discretized_points, attributes, nomeCol):

	import sys
	import numpy as np
	from sklearn.cluster import MeanShift, estimate_bandwidth
	from sklearn.datasets.samples_generator import make_blobs
	import mysql.connector
	import os
	import remove_files
	import shutil
	###############################################################################
	# Generate sample data
	
	con = mysql.connector.connect(user='biodados', password= 'sacizeir0', host= 'db', database='meanshift')
	cursor=con.cursor()
	
	
	if(attributes =="0"):
		
		arquivosaida = open("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/result", 'w')

		X = np.loadtxt(fn1, delimiter=';', dtype=bytes).astype(str)
		table_name = "result_MeanShift" + str(id)
		table= 'create table ' + table_name + '(ENSEMBL varchar(255), CLUSTER int, index ENS_idx(ENSEMBL));'
		cursor.execute(table)
		###############################################################################
		# Compute clustering with MeanShift
		#print(bandwidth)
		if(bandwidth == "AutoBandwidth"):
			# The following bandwidth can be automatically detected using
			bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
			#print("aqui")
		else:
			bandwidth = float(bandwidth)
			#print("aqui2")
		
		np.set_printoptions(threshold='nan')
			
		X= np.asarray(X, dtype=float)
		
		if(cluster_all == True):
			
			ms = MeanShift(bandwidth=bandwidth, bin_seeding=discretized_points, cluster_all=True, n_jobs = -1)
			arquivosaida.write("Discretized version of points: " + str(discretized_points) + '\n')
			arquivosaida.write("Cluster All: " + str(cluster_all) + '\n')
		else:
			ms = MeanShift(bandwidth=bandwidth, bin_seeding=discretized_points, cluster_all=False, n_jobs = -1)
			arquivosaida.write("Discretized version of points: " + str(discretized_points) + '\n')
			arquivosaida.write("Cluster All: " + str(cluster_all) + '\n')

		matriz= ms.fit_predict(X)

		labels = ms.labels_

		cluster_centers = ms.cluster_centers_
		labels_unique = np.unique(labels)
		n_clusters_ = len(labels_unique)
		#print("number of estimated clusters : %d" % n_clusters_)

		newmatriz = []

		arquivosaida.write("Number of clusters: " + str(n_clusters_) + '\n')
		arquivosaida.write("Bandwidth: " + str(bandwidth)+ '\n')

		for i in range(0,len(matriz)):
			#var= (str(genes[i]) + '\t' + str(matriz[i]))
			var= 'insert into ' + table_name + ' values("'+ str(genes[i])+'",'+str(matriz[i])+');'
			cursor.execute(var)
			arquivosaida.write(str(genes[i]) + '\t' + str(matriz[i])+ '\n')

		remove_table = 'drop table ' + table_name + ';'
		cursor.execute(remove_table)
	
		arquivosaida.close()

		os.rename("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/result", "/var/www/html/users/" + str(user)+ "/" + str(id)+ "/result.txt")
		arquivosaida_editar = open("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/result.txt", 'r')
		yourTxtFile = arquivosaida_editar.readlines()
		arquivosaida_editado = open("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/result", 'w')

		for line in yourTxtFile:
    			if not line.strip():
        			continue;
    			arquivosaida_editado.write(line)
		
		os.remove("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/result.txt")
		
		#remove_files.Remove_Files(user, id)

		return bandwidth
		
		
	else:
		table_name = "result_MeanShiftSelectAttributes" + str(id)
		table= 'create table ' + table_name + '(ENSEMBL varchar(255), '
		dir = '/var/www/html/users/' + user + '/' + str(id) + '/Resultados/'
		os.mkdir(dir)
		#print(nomeCol)
		for x in range(1, len(nomeCol)-1):
			table += nomeCol[x] + ' varchar(255), '
		
		#print(nomeCol)
		table+= nomeCol[len(nomeCol)-1] + ' varchar(255), index ENSEMBL_idx(ENSEMBL)); '
		#print(table)
		cursor.execute(table)
		bdw = bandwidth
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
			
			###############################################################################
			# Compute clustering with MeanShift
			#print(bandwidth)
			if(bdw == "AutoBandwidth"):
				# The following bandwidth can be automatically detected using
				bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
				saida2.write("Bandwidth: " + str(bandwidth) + '\n')
				#print("deu bom")
			
			else:
				bandwidth = float(bandwidth)
				saida2.write("Bandwidth: " + str(bandwidth) + '\n')
				#print("entrou")	
			#print(bandwidth)
			np.set_printoptions(threshold='nan')
				
			X= np.asarray(X, dtype=float)
			
			if(cluster_all == True):
				ms = MeanShift(bandwidth=bandwidth, bin_seeding=discretized_points, cluster_all=True, n_jobs = -1)
				saida2.write("Discretized version of points: " + str(discretized_points) + '\n')
				saida2.write("Cluster All: " + str(cluster_all) + '\n')
			else:
				ms = MeanShift(bandwidth=bandwidth, bin_seeding=discretized_points, cluster_all=False, n_jobs = -1)
				saida2.write("Discretized version of points: " + str(discretized_points) + '\n')
				saida2.write("Cluster All: " + str(cluster_all) + '\n')

			matriz= ms.fit_predict(X)

			labels = ms.labels_

			cluster_centers = ms.cluster_centers_
			labels_unique = np.unique(labels)
			n_clusters_ = len(labels_unique)
			#print("number of estimated clusters : %d" % n_clusters_)

			newmatriz = []

			saida2.write("Number of clusters: " + str(n_clusters_) + '\n')
			#saida2.write("Bandwidth: " + str(bandwidth)+ '\n')
			

			for i in range(0,len(matriz)):
				up = 'update ' + table_name + ' set ' + str(nomeCol[y]) + ' = ' + str(matriz[i])+ ' where ENSEMBL = "' + str(genes[i]) + '";'
				#print(up)
				cursor.execute(up)
				saida2.write(str(genes[i]) + '\t' + str(matriz[i])+ '\n')
		
		arquivototal = open('/var/www/html/users/' + user + '/' + str(id) + '/result', 'w')
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

#		remove_files.Remove_Files(user,id)



		return bandwidth
	##############################################################################
