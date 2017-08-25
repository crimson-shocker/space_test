#!/usr/bin/python3

import requests
import urllib3
import json

url = "https://api.cloudflare.com/client/v4/zones/1d4ed24975cbac674461013ae56daba1/dns_records"
sub = "-H 'X-Auth-Email: bkfonbetcom@gmail.com' -H 'X-Auth-Key: d3790e85d0a0e8886305904fac1bea543da48' -H 'Content-Type: application/json'"

sub_url = url + sub

data = {
        "type": "A",
        "name": "mp-29",
        "content": "188.42.196.185",
        "ttl": 1,
        "proxied": True
}

#data2 = "-H '{a}' -H '{a2}' -H '{c}' --data '{d}'".format(d=json.dumps(data), a="X-Auth-Email: bkfonbetcom@gmail.com", a2="X-Auth-Key: d3790e85d0a0e8886305904fac1bea543da48", c="Content-Type: application/json")
data2 = "--data '{d}'".format(d=json.dumps(data))

print(data2)



requests.post(sub_url, data=data2)
