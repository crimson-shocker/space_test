#!/usr/bin/env python3


num=64


with open("list.list", 'r') as f:
	ip_list=f.readlines()
	f.close

for i in ip_list:
	num+=1
	i=i.rstrip('\n')
	print('allow-hotplug agge:{num}'.format(num=num))
	print('auto agge:{num}'.format(num=num))
	print('iface agge:{num} inet static'.format(num=num))
	print('address {ip}'.format(ip=i))
	print('netmask 255.255.255.255')
	print('')
