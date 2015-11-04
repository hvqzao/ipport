#!/usr/bin/env python

'''
parse txt file with format:
IP1 PORT1
IP1 PORT2
IP2 PORT3
...

to nmap scan commands
'''

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	sys.stderr.write('Usage: '+sys.argv[0]+' <in-file>\n')
	sys.exit(1)

IPs=[]
PORTs=dict()
for i in open(sys.argv[1]).read().strip().split('\n'):
	if ' ' in i:
		IP,PORT = i.split(' ')
		#print IP,PORT
		if IP not in IPs:
			IPs += [IP]
		if IP not in PORTs.keys():
			PORTs[IP] = []
		if PORT not in PORTs[IP]:
			PORTs[IP] += [PORT]

for i in IPs:
	#print 'script -f -c "nmap -Pn -vv -sT -A --open -p',','.join(PORTs[i]),'-oA','done_us_tcp_ipports_nmap_results/us_tcp_'+i+'_nmap',i+'" done_us_tcp_ipports_nmap_results/us_tcp_'+i+'_nmap.log'
	print 'script -f -c "nmap -Pn -vv -sT -A --version-all -p',','.join(PORTs[i]),'-oA','done_us_tcp_ipports_nmap_results/us_tcp_'+i+'_nmap',i+'" done_us_tcp_ipports_nmap_results/us_tcp_'+i+'_nmap.log'
