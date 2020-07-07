#!/usr/local/anaconda2/bin/python2.7
import os
import cgi
import cgitb
cgitb.enable()
import json
import sys
import mysql.connector
import shutil
import kmeans

sys.stdout.write("Content-type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")

form = cgi.FieldStorage()

fn1 = "default"
#fn2 = "default"

cluster = form.getvalue("cluster")
max_iter = form.getvalue("max_iter")
User = form.getvalue("user")
tmm2 = form.getvalue("tmm2")
mrn2 = form.getvalue("mrn2")
fpkm2 = form.getvalue("fpkm2")
true_tpm2 = form.getvalue("true_tpm2")
tpm2 = form.getvalue("tpm2")
log2 = form.getvalue("log2")
attributes2 = form.getvalue("escolha2")
normalizacao3 = form.getvalue("normalizacao3")
normalizacao4 = form.getvalue("normalizacao4")



result = {}
if 'file1' in form:
	fileitem = form['file1']
	if fileitem.filename:
		fn1 = os.path.basename(fileitem.filename)
		file_path = "files/" + fn1
		arq = open(file_path, 'wb')
		arq.write(fileitem.file.read())
		arq.close()
		

con = mysql.connector.connect(user='biodados', password='sacizeir0', host='db', database= 'meanshift')
cursor = con.cursor()

if(fn1 != "default"):

	insert = 'insert into jobs_kmeans (nomeARQ, User, num_clusters, max_iter, status,tpm,log,attributes,normalizacao,normalizacao2,fpkm,true_tpm,tmm,mrn)values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s", "%s", "%s", "%s","%s");' % (fn1, User, cluster, max_iter, "0", tpm2,log2,attributes2,normalizacao3,normalizacao4,fpkm2,true_tpm2, tmm2,mrn2) 
	cursor.execute(insert)

	select = 'select last_insert_id();'
	cursor.execute(select)
#
	resu = cursor.fetchall()
	id = resu[0][0]

	insert2 = 'insert into alljobs (id,tipo) values ("%s","%s");' % (id,"KMeans")
	cursor.execute(insert2)

	select = 'select last_insert_id();'
	cursor.execute(select)
	resu = cursor.fetchall()
	id = resu[0][0]


	dir = ('users/' + User + '/' + str(id))
	os.mkdir(dir)

	shutil.copy2("files/" + fn1, dir)
#shutil.copy2("files/" + fn2, dir)

	result['success'] = True
	result['message'] = "File uploaded"
	result['id'] = id
#url = '<a href="jobs/' + str(id) + '/result">Download results</a>'
#result["url"] = url

	response = json.dumps(result, indent=1)

	sys.stdout.write(response)
	sys.stdout.write("\n")

	sys.stdout.close()

	saida = open("fileup.log", "w")
	for k in form:
		saida.write(k + "\n")

#url = '<a href="/jobs/' + str(id) + '/result">Download results</a>'
#print(url)
	saida.write("Fn1: " + fn1)
#saida.write("Fn2: " + fn2)
	saida.write(str(cluster))
#saida.write(form)
	saida.close()
	os.remove("files/" + fn1)	
#print(response)
#print("Successful communication")
