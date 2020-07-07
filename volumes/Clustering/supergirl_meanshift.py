import mysql.connector
import MShift
import math
from file_manipulation import filemanipulation
from file_manipulation import FPKM
from file_manipulation import TPM
from file_manipulation import LOG
from file_manipulation import NORMALIZACAO
from file_manipulation import NORMALIZACAO2
import os
import subprocess
import remove_files
import pandas as pd
from file_manipulation import tmm_norm
from file_manipulation import file_tmm_user
from file_manipulation import mrn_norm
from file_manipulation import file_mrn_user


con = mysql.connector.connect(user='biodados', password='sacizeir0', host='db', database= 'meanshift')
cursor = con.cursor()

sql = "update jobs_ms set status = 0 where status = 1;"
cursor.execute(sql)


print("Running jobs for Meanshift")

select = "select * from jobs_ms where status = 0;"
cursor.execute(select)
resultado = cursor.fetchall()

for line in resultado:
	if(True):	
		#print(line)
		id = line[0]
		
		select2 = "select * from alljobs where id = " + str(id)+ " and tipo = 'MeanShift';"
		cursor.execute(select2)
		resul = cursor.fetchall()
		pid = resul[0][0]		

		arq1 = line[1]
		user = line[2]
		cluster_all = line[3]
		bandwidth = line[4]
		attributes = line[6]
		tpm = line[7]
		logg = line[8]
		normalizacao = line[9]
		normalizacao2 = line[10]
		discretized_points = line[11]
		fpkm = line[12]
		true_tpm = line[13]
		tmm = line[14]
		mrn = line[15]

		print("Running Meanshift ID " + str(id)) 
		drop_table = "drop table if exists result_MeanShift" + str(id) + ";"
		cursor.execute(drop_table)
		update = "update jobs_ms set status = 1 where id ='" + str(id) + "';"
		cursor.execute(update)
		path1 = '/var/www/html/users/' + str(user) + "/" + str(pid) + '/' + arq1
		
		if(cluster_all == "1"):
				cluster_all=True
		else:
				cluster_all=False

		if(discretized_points == "1"):
			discretized_points = True
		else:
			discretized_points = False
		
		genes = []
		cabecalho = []
		print("Begin file manipulation")
	
		if(tmm == "1"):
			try:
				matrix = pd.read_table(path1, sep='\t')
				matrix.index = matrix.iloc[:,0]
				df = matrix.drop(matrix.columns[0], axis=1)
				normal_matrix = tmm_norm(df)
				path1 = '/var/www/html/users/' + str(user) + "/" + str(pid) + '/' + arq1+ "_TMM"
				normal_matrix.to_csv(path1,sep='\t', index=True, header=True)
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise


		
		filemanipulation(path1, genes, cabecalho)


		if(tmm == "1"):
			path2 = path1 + '_saida'
			file_tmm_user(path2, genes, cabecalho)
			path1 = '/var/www/html/users/' + str(user) + "/" + str(pid) + '/' + arq1
		else:
			path2 = path1 + '_saida'


		if(mrn == "1"):
			try:
				path2 = mrn_norm(path2, genes, cabecalho)
				#cabecalho[1:2] = []
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		
		if(fpkm == "1"):
			try:
				path2 = FPKM(path2, genes, cabecalho)
				cabecalho[1:2] = [] 
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise

		if(true_tpm == "1"):
			try:
				path2 = FPKM(path2, genes, cabecalho)
				cabecalho[1:2] = []
				path2 = TPM(path2, genes, cabecalho)
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise


		if(tpm == "1"):
			try:
				path2 = TPM(path2, genes, cabecalho)
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		if(logg == "1"):
			try:
				path2 = LOG(path2, genes, cabecalho)
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		if(normalizacao == "1"):
			try:
				path2 = NORMALIZACAO(path2, genes, cabecalho)
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		if(normalizacao2 == "1"):
			try:
				path2 = NORMALIZACAO2(path2, genes, cabecalho)
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise

		if ( (path2 != path1+'_saida') == True ):
			path_fim = path2 + "_user"
			try:
				subprocess.check_call(['Rscript', '/var/www/html/Boxplots.r', path1, path_fim, str(user), str(pid)], shell=False)
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		else:
			try:
				subprocess.check_call(['Rscript', '/var/www/html/Boxplots_input.r', path1, str(user), str(pid)], shell=False)
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		try:
		
			bdw = MShift.mshift(path2,genes,user,pid,bandwidth,cluster_all,discretized_points,attributes,cabecalho)
		

		except:

		#	pass
			try:
				drop_table = "drop table if exists result_MeanShift" + str(pid) + ";"
				cursor.execute(drop_table)
			#drop_table2 = "delete from alljobs where id = " + str(id)+ " and tipo = 'MeanShift';"
			#cursor.execute(drop_table2)
			#update =  "update jobs_ms set status = 1 where id ='" + str(id) + "';"
			#print (str(drop_table2) + 'aqui')
				update = "update jobs_ms set status = 1 where id ='" + str(id) + "';"
				cursor.execute(update)
				discretized_points = False
				print (discretized_points)
				bdw = MShift.mshift(path2,genes,user,pid,bandwidth,cluster_all,discretized_points,attributes,cabecalho)
				print ("foi")
		
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise

		if(attributes == "0"):
			path_result = "/var/www/html/users/" + str(user)+ "/" + str(pid)+ "/result"
			subprocess.check_call(['Rscript', '/var/www/html/Clustering_plot_MeanShift.r', path1, path_result , str(user), str(pid)], shell=False)

		#except:
		#	update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
		#	cursor.execute(update)
		#	raise

		if(bandwidth == "AutoBandwidth"):
			upbandwidth = "update jobs_ms set bandwidth = 'AutoBandwidth:" + str(bdw) + "' where id= " + str(id) + ";"
			cursor.execute(upbandwidth)	
			
		upstatus = "update jobs_ms set status = 2 where id='" + str(id) + "';"
		cursor.execute(upstatus)

		remove_files.Remove_Files(user, pid)
		
	else:
		update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
		cursor.execute(update)	
		raise
	
