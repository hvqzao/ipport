#!/usr/bin/env python

# changelog:
# Fri Feb 10 20:06:34 CET 2017  - introduced BLACKLISTED_PORTS option (can be commented out). 9100 is now excluded from scans based on ipport
# Wed Oct 12 10:19:15 CEST 2016 - "full" can be put in tag parameter to indicate scanning of all ports, instead of ipport, file with only IPs list can be provided.

'''
parse txt file with format:
IP1 PORT1
IP1 PORT2
IP2 PORT3
...

to nmap scan commands
'''

BLACKLISTED_PORTS=[9100,]

import sys
if len(sys.argv) > 2:
	tag = sys.argv[1]
	filename = sys.argv[2]
else:
	sys.stderr.write('Usage: '+sys.argv[0]+' <tag|full> <in-file>\n')
	sys.exit(1)

try:
    blacklisted_ports = map(lambda x: str(x), BLACKLISTED_PORTS)
except:
    blacklisted_ports = []

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
            ports = ','.join(filter(lambda x: x not in blacklisted_ports, PORTs[i]))
	print 'script -fac "nmap -Pn -vv -sT -A --version-all -p'+ports,'-oA',i+'_'+tag+'_nmap_tcp',i+'" '+i+'_'+tag+'_nmap_tcp.log'
	#                                       ^ --open
