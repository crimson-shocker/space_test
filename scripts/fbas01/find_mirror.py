#!/usr/local/bin/python3

import paramiko

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
