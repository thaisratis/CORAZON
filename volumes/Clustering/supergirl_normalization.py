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
import pandas as pd
from file_manipulation import tmm_norm
from file_manipulation import file_tmm_user
from file_manipulation import mrn_norm
from file_manipulation import file_mrn_user


con = mysql.connector.connect(user='biodados', password='sacizeir0', host='db', database= 'meanshift')
cursor = con.cursor()

sql = "update jobs_normalization set status = 0 where status = 1;"
cursor.execute(sql)


print("Running jobs for Normalization")

select = "select * from jobs_normalization where status = 0;"
cursor.execute(select)
resultado = cursor.fetchall()

for line in resultado:
	if(True):	
		#print(line)
		id = line[0]
		
		select2 = "select * from alljobs where id = " + str(id)+ " and tipo = 'Normalization';"
		cursor.execute(select2)
		resul = cursor.fetchall()
		pid = resul[0][0]		

		arq1 = line[1]
		tpm = line[2]
		logg = line[3]
		normalizacao = line[4]
		normalizacao2 = line[6]
		fpkm = line[7]
		true_tpm = line[8]
		tmm = line[9]
		mrn = line[10]

		print("Running Normalization ID " + str(id)) 
		update = "update jobs_normalization set status = 1 where id ='" + str(id) + "';"
		cursor.execute(update)
		path1 = '/var/www/html/users/Normalizations/' + str(pid) + '/' + arq1
		
		genes = []
		cabecalho = []
		print("Begin file manipulation")
	

		if(tmm == "1"):
			try:
				matrix = pd.read_table(path1, sep='\t')
				matrix.index = matrix.iloc[:,0]
				df = matrix.drop(matrix.columns[0], axis=1)
				normal_matrix = tmm_norm(df)
				path1 = '/var/www/html/users/Normalizations/' + "/" + str(pid) + '/' + arq1+ "_TMM"
				normal_matrix.to_csv(path1,sep='\t', index=True, header=True)
			except:
				update = "update jobs_normalization set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise



		filemanipulation(path1, genes, cabecalho)

		if(tmm == "1"):
			path2 = path1 + '_saida'
			file_tmm_user(path2, genes, cabecalho)
			path1 = '/var/www/html/users/Normalizations/' + str(pid) + '/' + arq1
			print("entrou")
		else:
			path2 = path1 + '_saida'


		if(mrn == "1"):
			try:
				path2 = mrn_norm(path2, genes, cabecalho)
			except:
				update = "update jobs_ms set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise


		if(fpkm == "1"):
			try:
				path2 = FPKM(path2, genes, cabecalho)
				cabecalho[1:2] = [] 
			except:
				update = "update jobs_normalization set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise

		if(true_tpm == "1"):
			try:
				path2 = FPKM(path2, genes, cabecalho)
				cabecalho[1:2] = []
				path2 = TPM(path2, genes, cabecalho)
			except:
				update = "update jobs_normalization set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise


		if(tpm == "1"):
			try:
				path2 = TPM(path2, genes, cabecalho)
			except:
				update = "update jobs_normalization set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		if(logg == "1"):
			try:
				path2 = LOG(path2, genes, cabecalho)
			except:
				update = "update jobs_normalization set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		if(normalizacao == "1"):
			try:
				path2 = NORMALIZACAO(path2, genes, cabecalho)
			except:
				update = "update jobs_normalization set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		if(normalizacao2 == "1"):
			try:
				path2 = NORMALIZACAO2(path2, genes, cabecalho)
			except:
				update = "update jobs_normalization set status = 3 where id ='" + str(id) + "';"
				cursor.execute(update)
				raise
		
		print("aqui")		
		result = os.rename(path2 + "_user", "/var/www/html/users/Normalizations/"+ str(pid) + "/result")
		print("renomeou")
		path_fim = "/var/www/html/users/Normalizations/"+ str(pid) + "/result"	

		subprocess.check_call(['Rscript', '/var/www/html/Boxplots.r', path1, path_fim, "Normalizations", str(pid)], shell=False)

		remove_files = '/var/www/html/users/Normalizations/' + str(pid) + '/'

		for x in os.listdir(remove_files):
			if ( ( 'result' not in (str(x)) ) and ('boxplot' not in (str(x))) ):
                        #print (str(remove_files) + str(x))
				os.remove(str(remove_files) + str(x))

		
		upstatus = "update jobs_normalization set status = 2 where id='" + str(id) + "';"
		cursor.execute(upstatus)
		
	else:
		update = "update jobs_normalization set status = 3 where id ='" + str(id) + "';"
		cursor.execute(update)	
		raise
	
