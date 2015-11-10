#!/usr/bin/env python

name = 'regular'

for ip,port in map(lambda x: x.split(' '), filter(lambda x: x[:1] != '#', map(lambda x: x.strip(), open('ports').read().strip().split('\n')))):
        cmd = 'time nmap -Pn -A -T4 --open -p '+port+' -oA '+name+'-'+ip+'-'+port+' '+ip
        #cmd = 'time nmap -T2 -vv -p1-63335 127.0.0.1'
        print 'screen -d -m -S '+name+'-'+ip+'-'+port+' script -f -c \''+cmd+'\' '+name+'-'+ip+'-'+port+'.log'
