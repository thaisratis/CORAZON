import mysql.connector
import kmeans
import math
import os
from file_manipulation import filemanipulation
from file_manipulation import FPKM
from file_manipulation import TPM
from file_manipulation import LOG
from file_manipulation import NORMALIZACAO
from file_manipulation import NORMALIZACAO2
import subprocess
import remove_files
import pandas as pd
from file_manipulation import tmm_norm
from file_manipulation import file_tmm_user
from file_manipulation import mrn_norm
from file_manipulation import file_mrn_user

con = mysql.connector.connect(user='biodados', password='sacizeir0', host='db', database= 'meanshift')
cursor = con.cursor()

sql2 = "update jobs_kmeans set status = 0 where status = 1;"
cursor.execute(sql2)

#print("Checking jobs for Kmeans")
select = "select * from jobs_kmeans where status = 0;"
cursor.execute(select)
resultado = cursor.fetchall()


for line in resultado:
	if(True):
		id = line[0]
		select2 = "select * from alljobs where id = " + str(id) + " and tipo = 'KMeans';"
		#print(str(select2))
		cursor.execute(select2)
		resul = cursor.fetchall()
				
		pid = resul[0][0]

		arq1 = line[1]
		user = line[2]
		num_cluster = line[3]
		max_iter = line[4]
		tpm2 = line[6]
		logg2 = line[7]
		attributes2 = line[8]
		normalizacao3 = line[9]
		normalizacao4 = line[10]
		fpkm2 = line[11]
		true_tpm2 = line[12]
		tmm2 = line[13]
		mrn2 = line[14]
		print("Running Kmeans ID " + str(id)) 
		
		drop_table = "drop table if exists result_KMeans" + str(id) + ";"
		cursor.execute(drop_table)
		
		update = "update jobs_kmeans set status = 1 where id ='" + str(id) + "';"
		cursor.execute(update)
		
		path1 = '/var/www/html/users/' + str(user) + "/" + str(pid) + '/' + arq1

		genes = []
		cabecalho = []


		if(tmm2 == "1"):
			try:
				matrix = pd.read_table(path1, sep='\t')
				matrix.index = matrix.iloc[:,0]
				df = matrix.drop(matrix.columns[0], axis=1)
				normal_matrix = tmm_norm(df)
				path1 = '/var/www/html/users/' + str(user) + "/" + str(pid) + '/' + arq1+ "_TMM"
				normal_matrix.to_csv(path1,sep='\t', index=True, header=True)
			except:
				update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise

		filemanipulation(path1, genes, cabecalho)

		
		if(tmm2 == "1"):
			path2 = path1 + '_saida'
			file_tmm_user(path2, genes, cabecalho)
			path1 = '/var/www/html/users/' + str(user) + "/" + str(pid) + '/' + arq1
		else:
			path2 = path1 + '_saida'

	
		if(mrn2 == "1"):
			try:
				path2 = mrn_norm(path2, genes, cabecalho)
				#cabecalho[1:2] = []
			except:
				update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise


		if(fpkm2 == "1"):
			try:
				path2 = FPKM(path2, genes, cabecalho)
				cabecalho[1:2] = []
			except:
				update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		if(true_tpm2 == "1"):
			try:
				path2 = FPKM(path2, genes, cabecalho)
				cabecalho[1:2] = []
				path2 = TPM(path2, genes, cabecalho)
			except:
				update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		if(tpm2 == "1"):
                        try:
                                path2 = TPM(path2, genes, cabecalho)
                        except:
                                update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
                                cursor.execute(update)
                                raise
                if(logg2 == "1"):
                        try:
                                path2 = LOG(path2, genes, cabecalho)
                        except:
                                update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
                                cursor.execute(update)
                                raise
                if(normalizacao3 == "1"):
                        try:
                                path2 = NORMALIZACAO(path2, genes, cabecalho)
                        except:
                                update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
                                cursor.execute(update)
                                raise
                if(normalizacao4 == "1"):
                        try:
                                path2 = NORMALIZACAO2(path2, genes, cabecalho)
                        except:
                                update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
                                cursor.execute(update)
                                raise
		

		if(num_cluster == 0):
			upstatus = "update jobs_kmeans set status = 3 where id='" + str(id) + "';"
			cursor.execute(upstatus)

		if ( (path2 != path1+'_saida') == True ):
			path_fim = path2 + "_user"
			try:
				subprocess.check_call(['Rscript', '/var/www/html/Boxplots.r', path1, path_fim, str(user), str(pid)], shell=False)
			except:
				update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise

		else:
			try:
				subprocess.check_call(['Rscript', '/var/www/html/Boxplots_input.r', path1, str(user), str(pid)], shell=False)
			except:
				update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise


		
		try:
			kms = kmeans.kMeans(path2,genes,user,pid,num_cluster,max_iter,attributes2,cabecalho)
			if(attributes2 == "0"):
				path_result = "/var/www/html/users/" + str(user)+ "/" + str(pid)+ "/result"
				subprocess.check_call(['Rscript', '/var/www/html/Clustering_plot_KmeansHierarchical.r', path1, path_result , str(user), str(pid)], shell=False)



		except:
			update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
			cursor.execute(update)
			raise

		upstatus = "update jobs_kmeans set status = 2 where id='" + str(id) + "';"
		cursor.execute(upstatus)

		remove_files.Remove_Files(user, pid)

	else:
		update = "update jobs_kmeans set status = 3 where id ='" + str(id) + "';"
		cursor.execute(update)
		raise

