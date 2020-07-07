import mysql.connector
import hierarchical
import math
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

sql2 = "update jobs_hierarchical set status = 0 where status = 1;"
cursor.execute(sql2)

select = "select * from jobs_hierarchical where status = 0;"
cursor.execute(select)
resultado = cursor.fetchall()


for line in resultado:
	if(True):
		id = line[0]
		select2 = "select * from alljobs where id = " + str(id) + " and tipo = 'hierarchical';"
		cursor.execute(select2)
		resul = cursor.fetchall()
				
		pid = resul[0][0]

		arq1 = line[1]
		user = line[2]
		num_cluster = line[3]
		linkage = line[4]
		tpm3 = line[6]
		log3 = line[7]
		attributes3 = line[8]
		normalizacao5 = line[9]
		normalizacao6 = line[10]
		fpkm3 = line[11]
		true_tpm3 = line[12]
		tmm3 = line[13]
		mrn3 = line[14]
		
		drop_table = "drop table if exists result_Hierarchical" + str(id) + ";"
		cursor.execute(drop_table)
		
		update = "update jobs_hierarchical set status = 1 where id ='" + str(id) + "';"
		cursor.execute(update)
		
		path1 = "/var/www/html/users/" + str(user) + "/" + str(pid) + "/" + arq1
		path2 = path1+'_saida'
		path3 = "/var/www/html/users/" + str(user) + "/" + str(pid) + "/" + arq1		

		genes = []
		cabecalho = []

		if(tmm3 == "1"):
			try:
				matrix = pd.read_table(path1, sep='\t')
				matrix.index = matrix.iloc[:,0]
				df = matrix.drop(matrix.columns[0], axis=1)
				normal_matrix = tmm_norm(df)
				path1 = '/var/www/html/users/' + str(user) + "/" + str(pid) + '/' + arq1+ "_TMM"
				normal_matrix.to_csv(path1,sep='\t', index=True, header=True)
				filemanipulation(path1, genes, cabecalho)
				path2 = path1 + '_saida'
				file_tmm_user(path2, genes, cabecalho)
				path1 = '/var/www/html/users/' + str(user) + "/" + str(pid) + '/' + arq1
				path3 = path2 + '_user'

			except:
				update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise

		
		if(mrn3 == "1"):
			try:
				if(tmm3 == "1"):
					path2 = path2
				else:
					filemanipulation(path1, genes, cabecalho)
					path2 = path1+ '_saida'
				
				path2 = mrn_norm(path2, genes, cabecalho)
				path3 = path2 + '_user'
				#cabecalho[1:2] = []
			except:
				update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise


		if(fpkm3 == "1"):
			try:
				if(tmm3 == "1" or mrn3 == "1"):
					path2 = path2
				
				else:
					filemanipulation(path1, genes, cabecalho)
					path2 = path1+ '_saida'

				path2 = FPKM(path2, genes, cabecalho)
				path3 = path2 + '_user'
				cabecalho[1:2] = []
			except:
				update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise

		if(true_tpm3 == "1"):
			try:
				if(fpkm3 == "1" or tmm3 == "1" or mrn3 == "1"):
					path2 = path2
				else:

					filemanipulation(path1, genes, cabecalho)
					path2 = path1+ '_saida'
				
				path2 = FPKM(path2, genes, cabecalho)
				path3 = path2 + '_user'
				cabecalho[1:2] = []
				path2 = TPM(path2, genes, cabecalho)
				path3 = path2 + '_user'

			except:
				update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
                                raise


		if(tpm3 == "1"):
			try:
				if(fpkm3 == "1" or true_tpm3 == "1" or tmm3 == "1" or mrn3 == "1"):
					path2 = path2
				else:
					filemanipulation(path1, genes, cabecalho)
					path2 = path1+'_saida'
				
				path2 = TPM(path2, genes, cabecalho)
				path3 = path2 + '_user'

			except:
				update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise

		if(log3 == "1"):
			try:
				if(tpm3 == "1" or fpkm3 == "1" or true_tpm3 == "1" or tmm3 == "1" or mrn3 == "1"):
					path2 = path2
				else:
					filemanipulation(path1, genes, cabecalho)
					path2 = path1+'_saida'
					
				path2 = LOG(path2, genes, cabecalho)
				print("path2")
				path3 = path2 + '_user'
			
			except:
				update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
					
		if(normalizacao5 == "1"):
			try:
				if(tpm3 == "1" or log3 == "1" or fpkm3 == "1" or true_tpm3 == "1" or tmm3 == "1" or mrn3 == "1"):
					path2 = path2
				else:
					filemanipulation(path1, genes, cabecalho)
					path2 = path1+'_saida'
					
				path2 = NORMALIZACAO(path2, genes, cabecalho)
				path3 = path2 + '_user'
				
			except:
				update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
					
		if(normalizacao6 == "1"):
			try:
				if(tpm3 == "1" or log3 == "1" or normalizacao5 == "1" or fpkm3 == "1" or true_tpm3 == "1" or tmm3 == "1" or mrn3 == "1"):
					path2 = path2
				else:
					filemanipulation(path1, genes, cabecalho)
					path2 = path1+'_saida'
					
				path2 = NORMALIZACAO2(path2, genes, cabecalho)
				path3 = path2 + '_user'
				
			except:
				update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		

		if ( (path2 != path1+'_saida') == True ):
			path_fim = path3
			try:
				subprocess.check_call(['Rscript', '/var/www/html/Boxplots.r', path1, path_fim, str(user), str(pid)], shell=False)
			except:
				update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		else:
			try:
				subprocess.check_call(['Rscript', '/var/www/html/Boxplots_input.r', path1, str(user), str(pid)], shell=False)
			except:
				update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise



		if(num_cluster == 0):
			upstatus = "update jobs_hierarchical set status = 3 where id='" + str(id) + "';"
			cursor.execute(upstatus)

		try:
			hie = hierarchical.Hierarchial(path3,user,pid,num_cluster,linkage,attributes3)
			if(attributes3 == "0"):
				path_result = "/var/www/html/users/" + str(user)+ "/" + str(pid)+ "/result"
				subprocess.check_call(['Rscript', '/var/www/html/Clustering_plot_KmeansHierarchical.r', path1, path_result , str(user), str(pid)], shell=False)



		except:
			update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
			cursor.execute(update)
			raise

		upstatus = "update jobs_hierarchical set status = 2 where id='" + str(id) + "';"
		cursor.execute(upstatus)

		remove_files.Remove_Files(user, pid)
		

	else:
		update = "update jobs_hierarchical set status = 3 where id ='" + str(id) + "';"
		cursor.execute(update)
		raise
