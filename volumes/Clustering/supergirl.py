#!/usr/local/anaconda2/bin/python2.7
import mysql.connector
import time
import os

con = mysql.connector.connect(user='biodados', password='sacizeir0', host='db', database= 'meanshift')
cursor = con.cursor()

inicio = True;

while(inicio):
	print("Checking jobs for Meanshift")
	select = "select * from jobs_ms where status = 0;"
	cursor.execute(select)
	resultado = cursor.fetchall()
	
	if(resultado != []):
		os.system("/usr/local/anaconda2/bin/python2.7 supergirl_meanshift.py")
	
	print("Checking jobs for Kmeans")
	select2 = "select * from jobs_kmeans where status = 0;"
	cursor.execute(select2)
	resultado2 = cursor.fetchall()
	
	if(resultado2 != []):
		os.system("/usr/local/anaconda2/bin/python2.7 supergirl_kmeans.py")

	print ("Checking jobs for Hierarchical")
	select3 = "select * from jobs_hierarchical where status =0;"
	cursor.execute(select3)
	resultado3 = cursor.fetchall()
	if(resultado3 != []):
		os.system("/usr/local/anaconda2/bin/python2.7 supergirl_hierarchical.py")

	print("Checking jobs for Normalization")
	select4 = "select * from jobs_normalization where status = 0;"
	cursor.execute(select4)
	resultado4 = cursor.fetchall()
	if(resultado4 != []):
		os.system("/usr/local/anaconda2/bin/python2.7 supergirl_normalization.py")

	else:
		time.sleep(20)
				
