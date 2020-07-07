#!/usr/local/anaconda2/bin/python2.7
import os
import cgi
import cgitb
cgitb.enable()
import json
import sys
import mysql.connector
import shutil
import MShift

sys.stdout.write("Content-type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")

form = cgi.FieldStorage()

fn1 = "default"
#fn2 = "default"

bdw = form.getvalue("txt")

if(bdw == ""):
	bdw = "AutoBandwidth"

cl_all= form.getvalue("testcluster_all")
User = form.getvalue("user")
attributes = form.getvalue("escolha")
tmm = form.getvalue("tmm")
mrn = form.getvalue("mrn")
fpkm = form.getvalue("fpkm")
true_tpm = form.getvalue("true_tpm")
tpm = form.getvalue("tpm")
log = form.getvalue("log")
normalizacao = form.getvalue("normalizacao")
normalizacao2 = form.getvalue("normalizacao2")
discretized_points = form.getvalue("discretized_points")

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

if(fn1!="default"):

	insert = 'insert into jobs_ms (nomeARQ, User, cluster_all, bandwidth, status, attributes,tpm,log,normalizacao,normalizacao2,discretized_points,fpkm,true_tpm,tmm,mrn)values("%s","%s","%s","%s","%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s","%s");' % (fn1, User, cl_all, bdw, "0", attributes, tpm, log, normalizacao, normalizacao2,discretized_points,fpkm,true_tpm,tmm,mrn) 
	cursor.execute(insert)

	select = 'select last_insert_id();'
	cursor.execute(select)
#
	resu = cursor.fetchall()
	id = resu[0][0]

	insert2 = 'insert into alljobs (id,tipo) values ("%s","%s");' % (id,"MeanShift")
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
	saida.write(str(cl_all))
#saida.write(form)
	saida.close()
	os.remove("files/" + fn1)
#print(response)
#print("Successful communication")
