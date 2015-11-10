#!/usr/bin/env python

'''
parse txt file with format:
IP1 PORT1
IP1 PORT2
IP2 PORT3
...

to nmap scan commands
'''

IPs=[]
PORTs=dict()
for i in open('scope_miniscan_ipports.txt').read().strip().split('\n'):
	IP,PORT = i.split(' ')
	#print IP,PORT
	if IP not in IPs:
		IPs += [IP]
	if IP not in PORTs.keys():
		PORTs[IP] = []
	if PORT not in PORTs[IP]:
		PORTs[IP] += [PORT]

for i in IPs:
	print 'nmap -Pn -vv -sT -sC -sV -O --open -p',','.join(PORTs[i]),'-aO','nmap-regular-'+i,i
