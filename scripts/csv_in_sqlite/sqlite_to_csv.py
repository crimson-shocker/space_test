#!/usr/bin/python3

import sqlite3

result = ""

conn = sqlite3.connect('app.db')
cur = conn.cursor()
data = cur.execute("select service, url, validate, service_caption, host_caption from monitoring")
q = data.fetchall()


with open('data.csv', "w") as f:
	for i in q:
		line = i[0]+";"+i[1]+";"+i[2]+";"+i[3]+";"+i[4]+"\n"
		result += line

	f.write(result)
	f.close
