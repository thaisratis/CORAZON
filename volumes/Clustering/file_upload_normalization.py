#!/usr/local/anaconda2/bin/python2.7
import os
import cgi
import cgitb
cgitb.enable()
import json
import sys
import mysql.connector
import shutil

sys.stdout.write("Content-type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")

form = cgi.FieldStorage()

fn1 = "default"

tmm = form.getvalue("tmm_normalization")
mrn = form.getvalue("mrn_normalization")
fpkm = form.getvalue("fpkm_normalization")
true_tpm = form.getvalue("true_tpm_normalization")
tpm = form.getvalue("tpm_normalization")
log = form.getvalue("log_normalization")
normalizacao = form.getvalue("normalizacao_normalization")
normalizacao2 = form.getvalue("normalizacao2_normalization")


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

#if( (fn1!="default") and (fpkm!="0") and(true_tpm!="0") and (tpm!="0") and (log!="0") and (normalizacao!="0") and (normalizacao2!= "0") ):
if( (fn1!="default") and ((tmm!="0") or (mrn!="0") or (fpkm!="0") or (true_tpm!="0") or (tpm!="0") or (log!="0") or (normalizacao!="0") or (normalizacao2!= "0"))):


	insert = 'insert into jobs_normalization (nomeARQ, tpm,log,normalizacao,status,normalizacao2,fpkm,true_tpm,tmm,mrn)values("%s","%s","%s","%s","%s", "%s", "%s", "%s", "%s", "%s");' % (fn1, tpm, log, normalizacao, "0", normalizacao2,fpkm,true_tpm,tmm,mrn) 
	cursor.execute(insert)

	select = 'select last_insert_id();'
	cursor.execute(select)

	resu = cursor.fetchall()
	id = resu[0][0]

	insert2 = 'insert into alljobs (id,tipo) values ("%s","%s");' % (id,"Normalization")
	cursor.execute(insert2)

	select = 'select last_insert_id();'
	cursor.execute(select)
	resu = cursor.fetchall()
	id = resu[0][0]

	dir = ('users/Normalizations/' + str(id))
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
	saida.close()
	os.remove("files/" + fn1)
