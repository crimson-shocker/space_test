#!/bin/bash

num1=$1
num2=$2


for i in {$num1..$num2}; do
	curl -X POST "https://api.cloudflare.com/client/v4/zones/1d4ed24975cbac674461013ae56daba1/dns_records" -H "X-Auth-Email: bkfonbetcom@gmail.com" -H "X-Auth-Key: d3790e85d0a0e8886305904fac1bea543da48" -H "Content-Type: application/json" --data \'{"type":"A","name":"mp-$i","content":"188.42.196.185","ttl":1,"proxied":true}\'
done
