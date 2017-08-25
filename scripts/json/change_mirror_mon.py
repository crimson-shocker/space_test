#!/usr/bin/python3

import json
import sys


MIRROR_ACTUAL = sys.argv[1]
MIRROR_TEST = sys.argv[2]

ACTUAL_WITH_OUT_DOT = MIRROR_ACTUAL.replace(".", "_")
TEST_WITH_OUT_DOT = MIRROR_TEST.replace(".", "_") 


with open('ban_mon_new.json', "r") as f:
	data = json.load(f)
	f.close

with open('ban_mon_new.json', "w") as e:
	data['mirror']['test']['with_dot'] = MIRROR_TEST
	data['mirror']['test']['with_out_dot'] = TEST_WITH_OUT_DOT
	data['mirror']['actual']['with_dot'] = MIRROR_ACTUAL
	data['mirror']['actual']['with_out_dot'] = ACTUAL_WITH_OUT_DOT
	json.dump(data, e, indent=4)
	e.close

	
