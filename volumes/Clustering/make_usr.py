#!/usr/local/bin/python3.3
import pymysql
import os
import cgi
import cgitb
from passlib.hash import pbkdf2_sha256
cgitb.enable()
import json
import sys

sys.stdout.write("Content-type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")

form = cgi.FieldStorage()

name = form.getvalue("Login")
passwd = form.getvalue("Senha")

if (passwd and name):
	hash = pbkdf2_sha256.encrypt(passwd, rounds=200000, salt_size=25)

	db = pymysql.connect(host = "db", user = "biodados", passwd = "sacizeir0", db = "meanshift")
	cur = db.cursor()
	sql = "select user from Users where user='" + name + "';"
	cur.execute(sql)
	results = cur.fetchall()
	if results == ():
		sql = "insert into Users values('%s','%s');" % (name, hash)
		cur.execute(sql)
		message = "New user created successfully"
		os.mkdir("users/" + name)
		os.chmod("users/" + name, 0o777)
		

	else:
		message = "Username already exists."

else:
	message = "Missing input"


results = {}

results['success'] = True
results['message'] = message

response = json.dumps(results, indent=1)

sys.stdout.write(message)

sys.stdout.close()

