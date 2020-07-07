#!/usr/local/anaconda2/bin/python2.7
import os
import cgi
import cgitb
cgitb.enable()
import json
import sys
import mysql.connector
import shutil
import hierarchical

sys.stdout.write("Content-type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")

form = cgi.FieldStorage()

fn1 = "default"

clusters = form.getvalue("cluster2")
linkage = form.getvalue("linkage")
User = form.getvalue("user")
tmm3 = form.getvalue("tmm3")
mrn3 = form.getvalue("mrn3")
fpkm3 = form.getvalue("fpkm3")
true_tpm3 = form.getvalue("true_tpm3")
tpm3 = form.getvalue("tpm3")
log3 = form.getvalue("log3")
attributes3 = form.getvalue("escolha3")
normalizacao5 = form.getvalue("normalizacao5")
normalizacao6 = form.getvalue("normalizacao6")



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

	insert = 'insert into jobs_hierarchical (nomeARQ, User, num_clusters, linkage, status,tpm,log,attributes,normalizacao,normalizacao2,fpkm,true_tpm,tmm,mrn)values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s", "%s", "%s", "%s","%s");' % (fn1, User, clusters, linkage, "0", tpm3,log3,attributes3,normalizacao5,normalizacao6, fpkm3, true_tpm3, tmm3, mrn3) 
	cursor.execute(insert)

	select = 'select last_insert_id();'
	cursor.execute(select)

	resu = cursor.fetchall()
	id = resu[0][0]

	insert2 = 'insert into alljobs (id,tipo) values ("%s","%s");' % (id,"hierarchical")
	cursor.execute(insert2)

	select = 'select last_insert_id();'
	cursor.execute(select)
	resu = cursor.fetchall()
	id = resu[0][0]


	dir = ('users/' + User + '/' + str(id))
	os.mkdir(dir)

	shutil.copy2("files/" + fn1, dir)

	result['success'] = True
	result['message'] = "File uploaded"
	result['id'] = id

	response = json.dumps(result, indent=1)

	sys.stdout.write(response)
	sys.stdout.write("\n")

	sys.stdout.close()

	saida = open("fileup.log", "w")
	for k in form:
		saida.write(k + "\n")

	saida.write("Fn1: " + fn1)

	saida.write(str(clusters))

	saida.close()
	os.remove("files/" + fn1)	
#print(response)
#print("Successful communication")
