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
if len(sys.argv) > 2:
    tag = sys.argv[1]
    filename = sys.argv[2]
else:
    sys.stderr.write('Usage: '+sys.argv[0]+' <tag> <in-file>\n')
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

for i in IPs:
    print('script -fac "nmap -Pn -vv -sU -A --version-all -p',','.join(PORTs[i]),'-oA',i+'_'+tag+'_nmap_udp',i+'" '+i+'_'+tag+'_nmap_udp.log')
    #                                       ^ --open
