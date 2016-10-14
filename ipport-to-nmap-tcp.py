#!/usr/bin/env python

# changelog:
# Wed Oct 12 10:19:15 CEST 2016 - "full" can be put in tag parameter to indicate scanning of all ports, instead of ipport, file with only IPs list can be provided.

'''
parse txt file with format:
IP1 PORT1
IP1 PORT2
IP2 PORT3
...

to nmap scan commands
'''

import sys
if len(sys.argv) > 2:
	tag = sys.argv[1]
	filename = sys.argv[2]
else:
	sys.stderr.write('Usage: '+sys.argv[0]+' <tag|full> <in-file>\n')
	sys.exit(1)

IPs=[]
PORTs=dict()
for i in open(filename).read().strip().split('\n'):
	if ' ' in i:
		IP,PORT = i.split(' ')
		#print IP,PORT
		if IP not in IPs:
			IPs += [IP]
		if IP not in PORTs.keys():
			PORTs[IP] = []
		if PORT not in PORTs[IP]:
			PORTs[IP] += [PORT]
        elif tag == 'full':
            IP = i.strip()
            if IP not in IPs:
                    IPs += [IP]

for i in IPs:
        if tag == 'full':
            ports = '0-65535'
        else:
            ports = ','.join(PORTs[i])
	print 'script -fac "nmap -Pn -vv -sT -A --version-all -p'+ports,'-oA',i+'_'+tag+'_nmap_tcp',i+'" '+i+'_'+tag+'_nmap_tcp.log'
	#                                       ^ --open
