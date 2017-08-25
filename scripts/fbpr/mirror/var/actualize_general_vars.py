#!/usr/bin/python3

import json
import sys

GENERAL_VARS="/srv/scripts/fbpr/mirror/var/gen_var.json"
TRASH_LIST="/srv/scripts/fbpr/mirror/var/trash_mirror_list.json"
WHITE_LIST="/srv/scripts/fbpr/mirror/var/white_mirror_list.json"

def open_json(open_json_file):
	with open(open_json_file, "r") as f:
		data_r=json.load(f)
		
	return data_r

def save_to_json(json_file, save_inf):
	with open(json_file, "w") as w:
		json.dump(save_inf, w, indent=4)
		w.close



gen_var=open_json(GENERAL_VARS)
stub_mirror_list=open_json(TRASH_LIST)
white_mirror_list=open_json(WHITE_LIST)


if len(white_mirror_list) > 0:
	print("Before actualize white mirror: ", len(white_mirror_list))
else:
	print("Error, not enough white mirror: ", len(white_mirror_list))
	sys.exit(1)

new_mirror=white_mirror_list[0]
banned_mirror=gen_var["mirror"]["actual_mirror"]
trash_mirror=gen_var["mirror"]["stub_mirror"]
act_mirror=gen_var["mirror"]["test_mirror"]



gen_var["mirror"]["actual_mirror"]=act_mirror
gen_var["mirror"]["test_mirror"]=new_mirror
gen_var["mirror"]["stub_mirror"]=banned_mirror

white_mirror_list.remove(new_mirror)
stub_mirror_list.append(trash_mirror)


save_to_json(GENERAL_VARS, gen_var)
save_to_json(TRASH_LIST, stub_mirror_list)
save_to_json(WHITE_LIST, white_mirror_list)

print("Mirror_left: ", len(white_mirror_list))
print("Actual_mirror: ", act_mirror)
print("Test_mirror: ", new_mirror)

