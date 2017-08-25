#!/usr/bin/python3

import CloudFlare
import sys


cf_login='bkfonbetcom@gmail.com'
cf_passwd='d3790e85d0a0e8886305904fac1bea543da48'
cf_id='1d4ed24975cbac674461013ae56daba1'

cf = CloudFlare.CloudFlare(email=cf_login, token=cf_passwd)


#data = {
#	"type": "A",
#	"name": "mp-30",
#	"content": "188.42.196.185",
#	"ttl": 1,
#	"proxied": True
#}

try:
	cf.zones.dns_records.post(cf_id, data={"type": "A", "name": "mp-30", "content": "188.42.196.185", "ttl": 1, "proxied": True})
except:
	sys.exit(0)
