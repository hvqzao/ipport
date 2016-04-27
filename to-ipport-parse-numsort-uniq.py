#!/usr/bin/env python
"""
sorts IP in file:

a.b.c.d port
e.f.g.h other_port

also parses nc and nmap "Discovered..." line, unicornscan and removes junk, e.g.

nc:

(UNKNOWN) [a.b.c.d] port (...) open

nmap / masscan:

Discovered open port port/tcp on a.b.c.d
Connect Scan Timing: About 1.16% done; ETC: 12:36 (1:26:25 remaining)

unicornscan:

TCP open a.b.c.d:e  ttl 128
TCP open                     ssh[ port]         from a.b.c.d  ttl 128

masscan (-oL):

open tcp e a.b.c.d 1447188919

"""

import re,sys
if len(sys.argv) < 2:
	sys.stderr.write('Usage: '+sys.argv[0]+' <in-file1> [in-file2] ...\n')
	sys.exit(1)

for path in sys.argv[1:]:
    # get directory
    if '/' in path:
        dirname = path[:path.rindex('/')+1]
        filename = path[path.rindex('/')+1:]
    else:
        dirname = ''
        filename = path
    # insert _ipport into save_as filename
    if '.' in filename:
        index = filename.rindex('.')
        save_as = '{}{}_ipport{}'.format(dirname, filename[:index], filename[index:])
        del index
    else:
        save_as = '{}{}_ipport'.format(dirname, filename)
    a = []
    for i in map(lambda x: x.strip(), open(path).read().strip().replace('\r','\n').split('\n')):
    	i = re.sub(r'^Discovered open port ([0-9]+)/tcp on ([0-9\.]+)$', r'\2 \1', i)
    	i = re.sub(r'^Discovered open port ([0-9]+)/udp on ([0-9\.]+)$', r'\2 \1', i)
    	i = re.sub(r'^\(UNKNOWN\) \[([0-9\.]+)\] ([0-9]+) \([^\)]*\) open', r'\1 \2', i)
    	i = re.sub(r'^TCP open ([0-9\.]+):([0-9]+)\s+ttl.*$', r'\1 \2', i)
    	i = re.sub(r'^TCP open\s+[^\[]+\[\s*([0-9]+)\]\s*from ([0-9\.]+)\s+ttl.*$', r'\2 \1', i)
    	i = re.sub(r'^open tcp ([0-9]+) ([0-9\.]+) [0-9]+$', r'\2 \1', i)
    	i = re.sub(r'^open udp ([0-9]+) ([0-9\.]+) [0-9]+$', r'\2 \1', i)
    	if re.match(r'^([0-9\.]+)\s*([0-9]+)$',i) != None:
    		i = re.sub(r'^([0-9\.]+)\s*([0-9]+)$',r'\1 \2',i)
    		ip,port = i.split(' ')
    		x = map(lambda x: int(x), ip.split('.') + [port])
    		if x not in a:
    			a += [x]
    a = map(lambda i: '.'.join(map(lambda x: str(x), i[:4]))+' '+str(i[4]), sorted(a))
    with open(save_as,'w') as f:
        for i in a:
            f.write('{}\n'.format(i))
    sys.stderr.write('{} saved.\n'.format(save_as))
