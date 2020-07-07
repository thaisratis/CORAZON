#!/usr/local/bin/python3.3
import pymysql
import os
import cgi
import cgitb
from passlib.hash import pbkdf2_sha256
cgitb.enable()
import json
import sys
import string
import random
import time

sys.stdout.write("Content-type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")

form = cgi.FieldStorage()
jobtable=""
jobtable2 =""
jobtable3 = ""
username = form.getvalue("Usuario")
passwd = form.getvalue("SenhaLogin")


db = pymysql.connect(host = "db", user = "biodados", passwd = "sacizeir0", db = "meanshift")
cur = db.cursor()

sql = "select password from Users where user='" + username + "';"
cur.execute(sql)
results = cur.fetchall()

message = ""
session_id = ""

if results == ():
	message = "Incorrect username"

else:
	hash = results[0][0]

	if pbkdf2_sha256.verify(passwd,hash):
		message = "Login successful"
		sql = "select ID,nomeARQ,cluster_all,bandwidth,status,Attributes,tpm,log,normalizacao,normalizacao2,discretized_points,fpkm,true_tpm,tmm,mrn from jobs_ms where user = '" + username + "' order by ID;"
		cur.execute(sql)
		results = cur.fetchall()
		if results == ():
			
                	jobtable = "<h2> MeanShift</h2></br>No jobs were found!"
		else:
			jobtable = """
	  <h2>MeanShift</h2></br>
	  <table id="t01">
	   <tr>
		<th>ID</th>
		<th>File</th>
		<th>Cluster All</th>
		<th>Discretized Points</th>
		<th>Bandwidth</th>
		<th>Attributes</th>
		<th>TMM</th>
		<th>MRN</th>
		<th>FPKM</th>
		<th>TPM</th>q
		<th>CPM</th>
		<th>Log</th>
		<th>Normalize</th>
		<th>Normalize by the highest value</th>
		<th>Status</th>
		<th>Result</th>
		<th>Boxplot</th>
		<th>Normalization file Boxplot</th>
		<th>Clustering Plot</th>
	   </tr>
			
	"""
		for line in results:
			curr_id = line[0]
			select2 = "select * from alljobs where id = " + str(curr_id) + " and tipo = 'MeanShift';"
			cur.execute(select2)
			resul = cur.fetchall()
			
			pid = resul[0][0]
			
			curr_file1 = line[1]
			#curr_file2 = line[2]
			curr_cluster_all = line[2]
			curr_bandwidth = line[3]
			curr_status = str(line[4])
			curr_attributes = str(line[5]) 
			curr_tpm = str(line[6])
			curr_log = str(line[7])
			curr_normalizacao = str(line[8])
			curr_normalizacao2 = str(line[9])
			curr_discretized_points = str(line[10])
			curr_fpkm = str(line[11])
			curr_true_tpm = str(line[12])
			curr_tmm = str(line[13])
			curr_mrn = str(line[14])

			file2 = curr_file1+ "_saida"
			curr_boxplot = "<a href = 'users/%s/%d/boxplot_bn.html'>Boxplot</a>" % (username, pid)



			if(curr_status == "0"):
				respostaStatus = "Queued"
			elif(curr_status == "1"):
				respostaStatus = "Running"
			elif(curr_status == "3"):
				respostaStatus = "Error in your data file!"
			else:
				respostaStatus = "Completed"
			
			if respostaStatus == "Completed":
                                curr_results = "<a href='users/%s/%d/result'>Download</a>" % (username, pid)
			#	curr_clustering = "<a href='users/%s/%d/Clustering.html'>Clustering Plot</a>" % (username, pid)
			else:
				curr_results = "Unavailable"
			#	curr_clustering = "Unavailable"
			
			if(curr_tmm == "1"):
				file2 = curr_file1+"_TMM_saida"
				curr_tmm = "<a href = 'users/%s/%d/%s'>TMM.txt</a>" % (username, pid, file2+"_user")
		
			if(curr_mrn == "1"):
				curr_mrn = "<a href = 'users/%s/%d/%s'>MRN.txt</a>" % (username, pid, file2+"_MRN_user")
				file2 = file2 + "_MRN"
			
			if(curr_fpkm == "1"):
				curr_fpkm = "<a href = 'users/%s/%d/%s'>FPKM.txt</a>" % (username, pid, file2+"_FPKM_user")
				file2 = file2+"_FPKM"

			if(curr_true_tpm == "1"):
                        	curr_true_tpm = "<a href = 'users/%s/%d/%s'>TPM.txt</a>" % (username, pid, file2+"_FPKM_TPM_user")
                        	file2 = file2 + "FPKM_TPM"


			if(curr_tpm == "1"):
				curr_tpm = "<a href = 'users/%s/%d/%s'>CPM.txt</a>" % (username, pid, file2+"_TPM_user")
				file2 = file2+"_TPM"

			if(curr_log == "1"):
				curr_log = "<a href = 'users/%s/%d/%s'>LOG.txt</a>" % (username, pid, file2+"_LOG_user")
				file2 = file2+"_LOG" 
			
			if(curr_normalizacao == "1"):
				curr_normalizacao = "<a href = 'users/%s/%d/%s'>NORM.txt</a>" % (username, pid, file2+"_normalizacao_user")
				file2 = file2+"_normalizacao"
			
			if(curr_normalizacao2 == "1"):
				curr_normalizacao2 = "<a href = 'users/%s/%d/%s'>NORMHV.txt</a>" % (username, pid, file2+"_normalizacao2_user")
				file2 = file2+"_normalizacao2"
			#else:
			#	curr_results = "Unavailable"
			if ( (file2 != str(curr_file1+ "_saida")) == True ):
				curr_normalized_boxplot = "<a href = 'users/%s/%d/boxplot_an.html'>Norm_Boxplot</a>" % (username, pid)
			else:
				curr_normalized_boxplot = "0"

			if( (curr_status == "2") and (curr_attributes == "0")):
				curr_clustering = "<a href='users/%s/%d/Clustering.html'>Clustering Plot</a>" % (username, pid)
			else:
				curr_clustering = "Unavailable"


			if(curr_cluster_all == "1"):
				curr_cluster_all = "True"
			else:
				curr_cluster_all = "False"

			if(curr_discretized_points == "1"):
				curr_discretized_points = "True"
			else:
				curr_discretized_points = "False"
			
			jobtable += """
   <tr>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   </tr>
""" % (str(pid), str(curr_file1), str(curr_cluster_all), str(curr_discretized_points), str(curr_bandwidth), str(curr_attributes), str(curr_tmm), str(curr_mrn), str(curr_fpkm), str(curr_true_tpm), str(curr_tpm), str(curr_log),str(curr_normalizacao),str(curr_normalizacao2), str(respostaStatus), str(curr_results), str(curr_boxplot), str(curr_normalized_boxplot), str(curr_clustering))
	
		sql = "select ID,nomeARQ,num_clusters,max_iter,status,attributes,tpm,log,normalizacao,normalizacao2,fpkm,true_tpm,tmm,mrn from jobs_kmeans where user = '" + username + "' order by ID;"
		cur.execute(sql)
		results = cur.fetchall()
		if results == ():
			jobtable2 = "<h2>K-Means</h2></br>No jobs were found!"
		else:
			jobtable2 = """
	<h2>K-Means</h2></br>
	  <table id="t02">
	   <tr>
		<th>ID</th>
		<th>File</th>
		<th>Num_clusters</th>
		<th>Max_iter</th>
		<th>Attributes</th>
		<th>TMM</th>
		<th>MRN</th>
		<th>FPKM</th>
		<th>TPM</th>
		<th>CPM</th>
		<th>Log</th>
		<th>Normalize</th>
		<th>Normalize by the highest value</th>
		<th>Status</th>
		<th>Result</th>
		<th>Boxplot</th>
		<th>Normalized file Boxplot</th>
		<th>Clustering Plot</th>
	   </tr>

	"""
			for line in results:
				curr_id = line[0]
				select2 = "select * from alljobs where id = " + str(curr_id) + " and tipo = 'KMeans';"
				cur.execute(select2)
				resul = cur.fetchall()
				pid =  resul[0][0]

				curr_file1 = line[1]
				curr_num_clusters = line[2]
				curr_max_iter = line[3]
				curr_status = str(line[4])
				curr_attributes = str(line[5])
				curr_tpm = str(line[6])
				curr_log = str(line[7])
				curr_normalizacao = str(line[8])
				curr_normalizacao2 = str(line[9])
				curr_fpkm = str(line[10])
				curr_true_tpm = str(line[11])
				curr_tmm = str(line[12])
				curr_mrn = str(line[13])

				file2 = curr_file1+ "_saida"
				curr_boxplot = "<a href = 'users/%s/%d/boxplot_bn.html'>Boxplot</a>" % (username, pid)

				if(curr_status == "0"):
					respostaStatus = "Queued"
				elif(curr_status == "1"):
					respostaStatus = "Running"
				elif(curr_status == "3"):
					respostaStatus = "Error in your data file!"
				else:
					respostaStatus = "Completed"

				if respostaStatus == "Completed":
					curr_results = "<a href='users/%s/%d/result'>Download</a>" % (username, pid)
				else:
					curr_results = "Unavailable"

				if(curr_tmm == "1"):
					file2 = curr_file1+"_TMM_saida"
					curr_tmm = "<a href = 'users/%s/%d/%s'>TMM.txt</a>" % (username, pid, file2+"_user")
		
				if(curr_mrn == "1"):
					curr_mrn = "<a href = 'users/%s/%d/%s'>MRN.txt</a>" % (username, pid, file2+"_MRN_user")
					file2 = file2 + "_MRN"

				if(curr_fpkm == "1"):
					curr_fpkm = "<a href = 'users/%s/%d/%s'>FPKM.txt</a>" % (username, pid, file2+"_FPKM_user")
					file2 = file2+"_FPKM"

				if(curr_true_tpm == "1"):
                        		curr_true_tpm = "<a href = 'users/%s/%d/%s'>TPM.txt</a>" % (username, pid, file2+"_FPKM_TPM_user")
                        		file2 = file2 + "_FPKM_TPM"


				if(curr_tpm == "1"):
					curr_tpm = "<a href = 'users/%s/%d/%s'>CPM.txt</a>" % (username, pid, file2+"_TPM_user")
					file2 = file2+"_TPM"
					
				if(curr_log == "1"):
					curr_log = "<a href = 'users/%s/%d/%s'>LOG.txt</a>" % (username, pid, file2+"_LOG_user")
					file2 = file2 + "_LOG"
					

				if(curr_normalizacao == "1"):
					curr_normalizacao = "<a href = 'users/%s/%d/%s'>NORM.txt</a>" % (username, pid, file2+"_normalizacao_user")
					file2 = file2+"_normalizacao"

				if(curr_normalizacao2 == "1"):
					curr_normalizacao2 = "<a href = 'users/%s/%d/%s'>NORMHV.txt</a>" % (username, pid, file2+"_normalizacao2_user")
					file2 = file2+"_normalizacao2"

				if ( (file2 != str(curr_file1+ "_saida")) == True ):
					curr_normalized_boxplot = "<a href = 'users/%s/%d/boxplot_an.html'>Norm_Boxplot</a>" % (username, pid)
				else:
					curr_normalized_boxplot = "0"

				if( (curr_status == "2") and (curr_attributes == "0")):
					curr_clustering = "<a href='users/%s/%d/Clustering.html'>Clustering Plot</a>" % (username, pid)
				else:
					curr_clustering = "Unavailable"


				jobtable2 += """

 <tr>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
   <td>%s</td>
  </tr>
""" % (str(pid), str(curr_file1), str(curr_num_clusters), str(curr_max_iter), str(curr_attributes), str(curr_tmm), str(curr_mrn), str(curr_fpkm), str(curr_true_tpm), str(curr_tpm), str(curr_log),str(curr_normalizacao),str(curr_normalizacao2), str(respostaStatus), str(curr_results), str(curr_boxplot), str(curr_normalized_boxplot), str(curr_clustering))


		sql = "select ID,nomeARQ,num_clusters,linkage,status,attributes,tpm,log,normalizacao,normalizacao2,fpkm,true_tpm,tmm,mrn from jobs_hierarchical where user = '" + username + "' order by ID;"
		cur.execute(sql)
		results = cur.fetchall()
		if results == ():
			jobtable3 = "<h2>Hierarchical</h2></br>No jobs were found!"
		else:
			jobtable3 = """
	<h2>Hierarchical</h2></br>
	  <table id="t03">
	   <tr>
		<th>ID</th>
		<th>File</th>
		<th>Num_clusters</th>
		<th>Linkage</th>
		<th>Attributes</th>
		<th>TMM</th>
		<th>MRN</th>
		<th>FPKM</th>
		<th>TPM</th>
		<th>CPM</th>
		<th>Log</th>
		<th>Normalize</th>
		<th>Normalize by the highest value</th>
		<th>Status</th>
		<th>Result</th>
		<th>Boxplot</th>
		<th>Normalized file Boxplot</th>
		<th>Clustering Plot</th>
	   </tr>

	"""
			for line in results:
				curr_id = line[0]
				select2 = "select * from alljobs where id = " + str(curr_id) + " and tipo = 'hierarchical';"
				cur.execute(select2)
				resul = cur.fetchall()
				pid =  resul[0][0]

				curr_file1 = line[1]
				curr_num_clusters = line[2]
				curr_linkage = line[3]
				curr_status = str(line[4])
				curr_attributes = str(line[5])
				curr_tpm = str(line[6])
				curr_log = str(line[7])
				curr_normalizacao = str(line[8])
				curr_normalizacao2 = str(line[9])
				curr_fpkm = str(line[10])
				curr_true_tpm =str(line[11])
				curr_tmm = str(line[12])
				curr_mrn = str(line[13])

				file2 = curr_file1+ "_saida"
				curr_boxplot = "<a href = 'users/%s/%d/boxplot_bn.html'>Boxplot</a>" % (username, pid)

				if(curr_status == "0"):
					respostaStatus = "Queued"
				elif(curr_status == "1"):
					respostaStatus = "Running"
				elif(curr_status == "3"):
					respostaStatus = "Error in your data file!"
				else:
					respostaStatus = "Completed"

				if respostaStatus == "Completed":
					curr_results = "<a href='users/%s/%d/result'>Download</a>" % (username, pid)
				else:
					curr_results = "Unavailable"


				if(curr_tmm == "1"):
					file2 = curr_file1+"_TMM_saida"
					curr_tmm = "<a href = 'users/%s/%d/%s'>TMM.txt</a>" % (username, pid, file2+"_user")
		
				if(curr_mrn == "1"):
					curr_mrn = "<a href = 'users/%s/%d/%s'>MRN.txt</a>" % (username, pid, file2+"_MRN_user")
					file2 = file2 + "_MRN"

				if(curr_fpkm == "1"):
					curr_fpkm = "<a href = 'users/%s/%d/%s'>FPKM.txt</a>" % (username, pid, file2+"_FPKM_user")
					file2 = file2+"_FPKM"

				if(curr_true_tpm == "1"):
                        		curr_true_tpm = "<a href = 'users/%s/%d/%s'>TPM.txt</a>" % (username, pid, file2+"_FPKM_TPM_user")
                        		file2 = file2 + "_FPKM_TPM"
				

				if(curr_tpm == "1"):
					curr_tpm = "<a href = 'users/%s/%d/%s'>CPM.txt</a>" % (username, pid, file2+"_TPM_user")
					file2 = file2+"_TPM"
					
				if(curr_log == "1"):
					curr_log = "<a href = 'users/%s/%d/%s'>LOG.txt</a>" % (username, pid, file2+"_LOG_user")
					file2 = file2 + "_LOG"
					

				if(curr_normalizacao == "1"):
					curr_normalizacao = "<a href = 'users/%s/%d/%s'>NORM.txt</a>" % (username, pid, file2+"_normalizacao_user")
					file2 = file2+"_normalizacao"

				if(curr_normalizacao2 == "1"):
					curr_normalizacao2 = "<a href = 'users/%s/%d/%s'>NORMHV.txt</a>" % (username, pid, file2+"_normalizacao2_user")
					file2 = file2+"_normalizacao2"
	
				if ( (file2 != str(curr_file1+ "_saida")) == True ):
					curr_normalized_boxplot = "<a href = 'users/%s/%d/boxplot_an.html'>Norm_Boxplot</a>" % (username, pid)
				else:
					curr_normalized_boxplot = "0"

				if( (curr_status == "2") and (curr_attributes == "0")):
					curr_clustering = "<a href='users/%s/%d/Clustering.html'>Clustering Plot</a>" % (username, pid)
				else:
					curr_clustering = "Unavailable"


			
				jobtable3 += """
	   <tr>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   <td>%s</td>
	   </tr>
	""" % (str(pid), str(curr_file1), str(curr_num_clusters), str(curr_linkage), str(curr_attributes), str(curr_tmm), str(curr_mrn), str(curr_fpkm), str(curr_true_tpm), str(curr_tpm), str(curr_log), str(curr_normalizacao), str(curr_normalizacao2), str(respostaStatus), str(curr_results), str(curr_boxplot), str(curr_normalized_boxplot), str(curr_clustering))

	
	else:
		message = "Incorrect password!"

result = {}
result['success'] = True
result['message'] = message
result['username'] = username
result['jobtable'] = jobtable
result['jobtable2'] = jobtable2
result['jobtable3'] = jobtable3

#result['sessionID'] = session_id

response = json.dumps(result, indent=1)

sys.stdout.write(response)
sys.stdout.write("\n")

sys.stdout.close()

