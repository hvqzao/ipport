#!/usr/bin/env python

'''
convert ip port list nmap commands sorrounded in script statements
'''

import sys,re
if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	sys.stderr.write('Usage: '+sys.argv[0]+' <in-file>\n')
	sys.exit(1)
ips = []
ports = dict()
for ip,port in map(lambda x: x.split(), filter(lambda x: re.match(r'^([0-9\.]+)\s*([0-9]+)$',x) != None, open(filename).read().strip().split('\n'))):
	if ip not in ips:
		ips += [ip]
	if ip not in ports.keys():
		ports[ip] = []
	ports[ip] += [port]	
for ip in ips:
	#screen = 'screen -d -m -S '+ip+'-nmap-tcp-discovered '
	print 'script -f -c \'nmap -Pn -A -vv -p'+','.join(ports[ip])+' -oA '+ip+'-nmap-tcp-discovered '+ip+'\' '+ip+'-nmap-tcp-discovered.log'
