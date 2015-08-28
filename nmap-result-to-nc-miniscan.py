#!/usr/bin/env python

'''
convert regular .nmap results to netcat miniscan
'''

dane = open('results.nmap').read().strip().split('\n')
IP = None
ports = []
print '{'
while dane:
	line = dane.pop(0)
	#print line
	SCAN = 'Nmap scan report for '
	if line[:len(SCAN)] == SCAN:
		if IP != None:
			#print 'nmap -Pn -sT -A -vv -p',','.join(ports),'-oA',IP+'__'+'_'.join(ports),IP
			for port in ports:
				print 'nc -zvnw 1 '+IP+' '+port+' 2>&1 &'
		ports = []
		IP = line[len(SCAN):]
	if IP != None and '/tcp' in line:
		port = line.split('/')[0]
		ports += [port]
print '} | grep open'
