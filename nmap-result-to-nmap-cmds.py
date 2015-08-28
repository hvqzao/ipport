#!/usr/bin/env python

'''
convert regular .nmap file to nmap commands 
'''

dane = open('results.nmap').read().strip().split('\n')
IP = None
ports = []
while dane:
	line = dane.pop(0)
	#print line
	SCAN = 'Nmap scan report for '
	if line[:len(SCAN)] == SCAN:
		if IP != None:
			print 'nmap -Pn -T4 -A -vv -p',','.join(ports),'-oA',IP,IP # IP+'__'+'_'.join(ports)
		ports = []
		IP = line[len(SCAN):]
	if IP != None and '/tcp' in line:
		port = line.split('/')[0]
		ports += [port]
