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

pid = form.getvalue("GuestJob")
message = ""
message2 = ""
message3 = ""
message4 = ""

db = pymysql.connect(host = "db", user = "biodados", passwd = "sacizeir0", db = "meanshift")
cur = db.cursor()


sqlall = "select * from alljobs where pid= " + str(pid) + ';'
cur.execute(sqlall)
results = cur.fetchall()

tipo=""

try:
	id = results[0][1]
except:
	message = "Invalid ID!"

try:
	tipo = results[0][2]
except:
	message = "Invalid ID!"


if (tipo == "MeanShift"):
	tabela = "jobs_ms"

elif (tipo == "hierarchical"):
	tabela = "jobs_hierarchical"

elif (tipo == "KMeans"):
	tabela = "jobs_kmeans"

else:
	tabela = "jobs_normalization"
	
if(tabela == "jobs_normalization"):
	sql = "select * from " + tabela + " where id='" + str(id) + "';"

else:
	sql = "select * from " + tabela + " where id='" + str(id) + "'and User = 'Guest';"

cur.execute(sql)
results = cur.fetchall()

if(results!=()):
	for line in results:
		curr_status = str(line[5])
		if(curr_status == "0"):
			message = "Queued"
		elif(curr_status == "1"):
			message = "Running"
		elif(curr_status == "3"):
			message = "Error in your data file!"
		else:
			if(tabela == "jobs_normalization"):
				message = "<a href='users/Normalizations/%s/result'>Download</a>" % (pid)
				message2 = "<a href='users/Normalizations/%s/boxplot_bn.html'>Boxplot</a>" % (pid)
				message3 = "<a href='users/Normalizations/%s/boxplot_an.html'>Normalized Boxplot</a>" % (pid)
				#message4 = "<a href='users/Guest/%s/Clustering.html'>Clustering</a>" % (pid)

			else:
				message = "<a href='users/Guest/%s/result'>Download</a>" % (pid)
				message2 = "<a href='users/Guest/%s/boxplot_bn.html'>Boxplot</a>" % (pid)
				message3 = "<a href='users/Guest/%s/boxplot_an.html'>Normalized Boxplot</a>" % (pid)
				message4 = "<a href='users/Guest/%s/Clustering.html'>Clustering</a>" % (pid)
				
				file_path = '/var/www/html/users/Guest/%s/boxplot_an.html' %(pid)
				if( (os.path.isfile(file_path)) == True) :
        				message3 = "<a href='users/Guest/%s/boxplot_an.html'>Normalized Boxplot</a>" % (pid)
				else:
					message3 = "No normalization was selected"

				file_path2 = '/var/www/html/users/Guest/%s/Clustering.html' %(pid)
				if( (os.path.isfile(file_path2)) == True) :
					message4 = "<a href='users/Guest/%s/Clustering.html'>Clustering</a>" % (pid)
				else:
					message4 = "Unavailable if Combination of all attributes -1 selected"




else:
	message = "Invalid ID!"


result = {}
result['success'] = True
result['message'] = message
result['message2'] = message2
result['message3'] = message3
result['message4'] = message4

response = json.dumps(result, indent=1)
sys.stdout.write(response)
sys.stdout.write("\n")

sys.stdout.close()	

