#!/usr/bin/env python3
import urllib.request
import sys
import os
import json
import paramiko

GENERAL_WARS="/etc/ansible/vars/auto_change_vars.json"
AP="/etc/ansible/vars/ap.json"
LP="/etc/ansible/vars/lp.json"
MP_FOR_ALL="/etc/ansible/vars/mp_for_all.json"
MP_ADV="/etc/ansible/vars/mp_adv.json"


# --- open http site ---
ban_list_url = 'https://raw.githubusercontent.com/zapret-info/z-i/master/dump.csv'
DATA = urllib.request.urlopen(ban_list_url)
#/ --- open http site ---

ban_data = str(DATA.read())

#---Find_mirror_and_old-mirror---
host = 'fbpr01.fbtools.cc'
user = "root"
passwd = "Q7k20-RBa!"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname = host, username = user, password=passwd)
stdin, stdout, stderr = client.exec_command('ls -1 /etc/nginx/vhosts/_mirror-ordinary/8_stub/ | head -1')
stub = stdout.read() + stderr.read()
stdin, stdout, stderr = client.exec_command('ls -1 /etc/nginx/vhosts/_mirror-ordinary/3_in-use/ | head -1')
actual = stdout.read() + stderr.read()
client.close()

stub = stub.decode("utf-8")
stub = stub.replace("\n", "")
actual = actual.decode("utf-8")
actual = actual.replace("\n", "")
print("Actual: ", actual)
print("Stub: ", stub)
#/


#---Find_Landings---
def save_to_json(json_file, number, sub_data, dmn_data ):
	json_data=[]
	number = int(number)
	for i in range(1, number, 1):
#		print("for save_i:" ,i)
		if i<10:
			i=str(i)
			json_data.append(sub_data+"0"+i+dmn_data)
#			print("for save:", sub_data+"0"+i+dmn_data)
		else:
			i=str(i)
			json_data.append(sub_data+i+dmn_data)
#			print("for save:", sub_data+i+dmn_data)


	with open(json_file, "w") as e:
		json.dump(json_data, e, indent=4)
		e.close



def load_json(json_file):
	with open(json_file, "r") as r:
		data_r=json.load(r)
	
	return data_r


def find_actual_landing(landing_sub, landing_num, landing_dmn, banned_data):
	sub = landing_sub
#	if int(landing_num)<10:
#		num=str(int(landing_num))
#		num="0"+num
#	else:
#		num=str(int(landing_num))
#		num=num
	
	num = landing_num
	dmn = landing_dmn
	while True:
		num = int(num)
		if int(num) < 10:
			num = str(num)
			num = "0" + num
		else:
			num = str(num)

		if sub+num+dmn in banned_data:
			print("Bunned_landing:"+sub+num+dmn)
			num = str(int(num)+1)
		else:
			print("Actual_landing:"+sub+num+dmn)
#			if int(num)<10:
#				actual_landing = sub+"0"+num+dmn
#			else:
#				actual_landing = sub+num+dmn
			actual_landing = sub+num+dmn

			break

	return {"num": num, "actual_landing": actual_landing}


gen_var=load_json(GENERAL_WARS)
ap_num = gen_var['ap']['num']
ap_sub = gen_var['ap']['sub']
ap_dmn = gen_var['ap']['dmn']

lp_num = gen_var['lp']['num']
lp_sub = gen_var['lp']['sub']
lp_dmn = gen_var['lp']['dmn']

mp_for_all_num = gen_var['mp_for_all']['num']
mp_for_all_sub = gen_var['mp_for_all']['sub']
mp_for_all_dmn = gen_var['mp_for_all']['dmn']

mp_adv_num = gen_var['mp_adv']['num']
mp_adv_sub = gen_var['mp_adv']['sub']
mp_adv_dmn = gen_var['mp_adv']['dmn']




#while True:
#	if ap_sub+ap_num+ap_dmn in ban_data:
#		print("Bunned_landing:"+ap_sub+ap_num+ap_dmn)
#		ap_num = str(int(ap_num)+1)
#	else:
#		print("Actual_landing:"+ap_sub+ap_num+ap_dmn)
#		actual_ap = ap_sub+ap_num+ap_dmn
#		break


data_ap = find_actual_landing(gen_var['ap']['sub'], gen_var['ap']['num'], gen_var['ap']['dmn'], ban_data)
print(data_ap["actual_landing"])
print(data_ap["num"])
print("---===---")

data_lp = find_actual_landing(gen_var['lp']['sub'], gen_var['lp']['num'], gen_var['lp']['dmn'], ban_data)
print(data_lp["actual_landing"])
print(data_lp["num"])
print("---===---")

data_mp_for_all = find_actual_landing(gen_var['mp_for_all']['sub'], gen_var['mp_for_all']['num'], gen_var['mp_for_all']['dmn'], ban_data)
print(data_mp_for_all["actual_landing"])
print("after find:", data_mp_for_all["num"])
print("---===---")

data_mp_adv = find_actual_landing(gen_var['mp_adv']['sub'], gen_var['mp_adv']['num'], gen_var['mp_adv']['dmn'], ban_data)
print(data_mp_adv["actual_landing"])
print(data_mp_adv["num"])
print("---===---")



with open(GENERAL_WARS, "w") as w:
	gen_var['ap']['num'] = data_ap["num"]
	gen_var['lp']['num'] = data_lp["num"]
	gen_var['mp_for_all']['num'] = data_mp_for_all["num"]
	gen_var['mp_adv']['num'] = data_mp_adv["num"]
	gen_var['mirror']['actual'] = actual
	gen_var['mirror']['stub'] = stub
	json.dump(gen_var, w, indent=4)
	w.close



save_to_json(LP, gen_var['lp']['num'], gen_var['lp']['sub'], gen_var['lp']['dmn'])
save_to_json(AP, gen_var['ap']['num'], gen_var['ap']['sub'], gen_var['ap']['dmn'])
save_to_json(MP_FOR_ALL, gen_var['mp_for_all']['num'], gen_var['mp_for_all']['sub'], gen_var['mp_for_all']['dmn'])
save_to_json(MP_ADV, gen_var['mp_adv']['num'], gen_var['mp_adv']['sub'], gen_var['mp_adv']['dmn'])
