def Hierarchial(fn1, user, id, num_cluster, method, attributes):
	
	import numpy as np
	import sys
	import mysql.connector
	import os
	import subprocess
	import remove_files
	
	con = mysql.connector.connect(user='biodados', password= 'sacizeir0', host= 'db', database='meanshift')
	cursor=con.cursor()
	
	if(method == 1):
		methodology = "ward.D"
	elif(method == 2):
		methodology = "ward.D2"
	elif(method == 3):
		methodology = "single"
	elif(method == 4):
		methodology = "complete"
	elif(method == 5):
		methodology = "average"
	elif(method == 6):
		methodology = "mcquitty"
	elif(method == 7):
		methodology = "median"
	elif(method == 8):
		methodology = "centroid"	
		

	if(attributes =="0"):
		arquivosaida = open("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/result", 'a')

		table_name = "result_Hierarchical" + str(id)
		table= 'create table ' + table_name + '(ENSEMBL varchar(255), CLUSTER int, index ENS_idx(ENSEMBL));'
		cursor.execute(table)
		sys.stdout = open ("arquivo", "w")
			
		cutoff = num_cluster

		arquivosaida.writelines("Number of clusters: " + str(cutoff) + '\n')		
		arquivosaida.writelines("Method: " + str(methodology)+ '\n')	

		subprocess.check_call(['Rscript', '/var/www/html/hierarchical.r', fn1, str(methodology), str(cutoff), str(user), str(id)], shell=False)

		arquivosaidahierarchical = open("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/teste", 'r')
		arquivosaidahierarchical.readline()

		for line in arquivosaidahierarchical:
			arquivosaida.writelines(str(line))
			linha = line.split('\t')
			var= 'insert into ' + table_name + ' values("'+ str(linha[0])+'",'+str(linha[1])+');'
			cursor.execute(var)
		
		arquivosaida.close()
		os.remove("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/teste")
		remove_table = 'drop table ' + table_name + ';'
		cursor.execute(remove_table)

	
	else:
		
		table_name = "result_HierarchicalSelectAttributes" + str(id)
		table= 'create table ' + table_name + '(ENSEMBL varchar(255), '
		dir = '/var/www/html/users/' + user + '/' + str(id) + '/Resultados/'		
		os.mkdir(dir)
		
		cabecalho = []
		genes = []
		cutoff = num_cluster

		arquivo = open(fn1, 'r').readlines()

		for x in range(0,len(arquivo)):
			if(x == 0):
				cabecalho=arquivo[x].replace(" ", "_").strip().split('\t')
				
				
			else:
				genes.append(arquivo[x].split('\t')[0])
		
		#print(cabecalho)

		for x in range(1, len(cabecalho)-1):
			table += cabecalho[x] + ' varchar(255), '


		table+= cabecalho[len(cabecalho)-1] + ' varchar(255), index ENSEMBL_idx(ENSEMBL)); '
		
		#print(table)
		droptable = "drop table if exists " + table_name + ";"
		cursor.execute(droptable) 
		cursor.execute(table)

			
		for x in range(0,len(genes)):
			var= 'insert into ' + table_name + ' (ENSEMBL) values("'+ str(genes[x])+ '");'
			cursor.execute(var)



		for y in range(1,len(cabecalho)):
			print('eliminando coluna: ' + str(cabecalho[y])+ '\n')
			cut = "cat " + fn1 + " | cut -f "
			for i in range (1,len(cabecalho)):
				if(i != y):
					cut+= str(i+1) + ','
			cut = cut[:-1]
			
			saida = dir + 'result_' + user + '_' + str(id) + '_' + str(y)
			cutsaida = cut + ' > ' + saida
			#print(cutsaida)
			os.system(cutsaida)
			
			arquivosaida = open("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/result", 'w')
			
			arquivosaida.writelines("Number of clusters: " + str(cutoff) + '\n')		
			arquivosaida.writelines("Method: " + str(methodology)+ '\n\n')	
			
			for j in cabecalho:
				arquivosaida.write(j + '\t')
			arquivosaida.write('\n')

			subprocess.check_call(['Rscript', '/var/www/html/hierarchical.r', fn1, str(methodology), str(cutoff), str(user), str(id)], shell=False)

			arquivosaidahierarchical = open("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/teste", 'r')
			arquivosaidahierarchical.readline()

			for line in arquivosaidahierarchical:
				linha = line.split('\t')
				up = 'update ' + table_name + ' set ' + str(cabecalho[y]) + ' = ' + str(linha[1])+ ' where ENSEMBL = "' + str(linha[0]) + '";'
				#print(up)
				cursor.execute(up)
			
			select = 'select * from ' + table_name + ';'
			cursor.execute(select)
			resultado = cursor.fetchall()
			for linha in resultado:
				for i in linha:
					arquivosaida.write(str(i) + '\t')
				arquivosaida.write('\n')

			arquivosaida.close()
			arquivosaidahierarchical.close()
		os.remove("/var/www/html/users/" + str(user)+ "/" + str(id)+ "/teste")
		
		remove_table = 'drop table ' + table_name + ';'
		cursor.execute(remove_table)

#	remove_files.Remove_Files(user, id)


