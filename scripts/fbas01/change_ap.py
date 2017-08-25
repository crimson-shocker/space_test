#!/usr/bin/python3

import json
import sys


sub="ap-"
fqdn=".access-fonbet.com"

json_data=[]

for i in range(1, 12, 1):
	if i<10:
		i=str(i)
		json_data.append(sub+"0"+i+fqdn)
	else:
		i=str(i)
		json_data.append(sub+i+fqdn)


with open('ap.json', "w") as e:
	json.dump(json_data, e, indent=4)
	e.close

