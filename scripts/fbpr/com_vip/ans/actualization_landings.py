#!/usr/bin/env python3
import urllib.request
import sys
import os
import json
import CloudFlare

GENERAL_WARS="/etc/ansible/vars/com_vip/gen_var.json"
MIRROR_COM="/etc/ansible/vars/com_vip/dotcom.json"
MIRROR_VIP="/etc/ansible/vars/com_vip/dotvip.json"

# --- open http site ---
ban_list_url = 'https://raw.githubusercontent.com/zapret-info/z-i/master/dump.csv'
DATA = urllib.request.urlopen(ban_list_url)
ban_data = str(DATA.read())
#/ --- open http site ---

#1
def load_json(json_file):
	with open(json_file, "r") as r:
		data_r=json.load(r)
	
	return data_r
'''
def remove_banned_mirror(fir, thi):
	with open(thi, "r") as re:
		read_data = json.load(re)
		read_data.remove(fir)
		with open(thi, "w") as wr:
			json.dump(read_data, wr, indent=4)
		wr.close
	re.close
'''
mirror_to_remove = []
def find_actual_landing(landing_sub, landing_num, landing_dmn, banned_data, file_mirror_com_and_vip):
	sub = landing_sub
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
			mirror_to_remove.append(sub+num+dmn)
#			remove_banned_mirror(sub+num+dmn, file_mirror_com_and_vip)
			stub_mirror = sub+num+dmn
			print("Bunned_mirror:"+sub+num+dmn)
			num = str(int(num)+1)
		else:
			print("Actual_mirror:"+sub+num+dmn)
			actual_landing = sub+num+dmn

			break

	return {"num": num, "actual_landing": actual_landing, "stub": stub_mirror}

#/1

#2
gen_var=load_json(GENERAL_WARS)
mirror_com_num = gen_var['com']['num']
mirror_com_sld = gen_var['com']['sld']
mirror_com_tld = gen_var['com']['tld']

mirror_vip_num = gen_var['vip']['num']
mirror_vip_sld = gen_var['vip']['sld']
mirror_vip_tld = gen_var['vip']['tld']
#/2
#3


data_com = find_actual_landing(gen_var['com']['sld'], gen_var['com']['num'], gen_var['com']['tld'], ban_data, MIRROR_COM)
print(data_com["actual_landing"])
print(data_com["num"])
print("---===---")

data_vip = find_actual_landing(gen_var['vip']['sld'], gen_var['vip']['num'], gen_var['vip']['tld'], ban_data, MIRROR_VIP)
print(data_vip["actual_landing"])
print(data_vip["num"])
print("---===---")
#/3

print(mirror_to_remove)

#4
with open(GENERAL_WARS, "w") as w:
	gen_var['com']['num'] = data_com["num"]
	gen_var['vip']['num'] = data_vip["num"]
	gen_var['com']['act'] = data_com["actual_landing"]
	gen_var['vip']['act'] = data_vip["actual_landing"]
	gen_var['com']['stub'] = data_com["stub"]
	gen_var['vip']['stub'] = data_vip["stub"]
	json.dump(gen_var, w, indent=4)
	w.close
#/4


com_domain = load_json(MIRROR_COM)
vip_domain = load_json(MIRROR_VIP)

com_result = list(set(com_domain).difference(set(mirror_to_remove)))
vip_result = list(set(vip_domain).difference(set(mirror_to_remove)))

with open(MIRROR_COM, "w") as com:
	json.dump(com_result, com, indent=4)
	com.close

with open(MIRROR_VIP, "w") as vip:
	json.dump(vip_result, vip, indent=4)
	vip.close



'''




'''
