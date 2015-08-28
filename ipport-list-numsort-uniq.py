#!/usr/bin/env python
"""
sorts IP in file:

a.b.c.d port
e.f.g.h other_port

also parses nc and nmap "Discovered..." line, unicornscan and removes junk, e.g.

nc:

(UNKNOWN) [a.b.c.d] port (...) open

nmap:

Discovered open port port/tcp on a.b.c.d
Connect Scan Timing: About 1.16% done; ETC: 12:36 (1:26:25 remaining)

unicornscan:

TCP open a.b.c.d:e  ttl 128
TCP open                     ssh[ port]         from a.b.c.d  ttl 128
"""

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	sys.stderr.write('Usage: '+sys.argv[0]+' <in-file>\n')
	sys.exit(1)

import re
a = []
for i in map(lambda x: x.strip(), open(filename).read().strip().split('\n')):
	i = re.sub(r'^Discovered open port ([0-9]+)/tcp on ([0-9\.]+)$', r'\2 \1', i)
	i = re.sub(r'^\(UNKNOWN\) \[([0-9\.]+)\] ([0-9]+) \([^\)]*\) open', r'\1 \2', i)
	i = re.sub(r'^TCP open ([0-9\.]+):([0-9]+)\s+ttl.*$', r'\1 \2', i)
	i = re.sub(r'^TCP open\s+[^\[]+\[\s*([0-9]+)\]\s*from ([0-9\.]+)\s+ttl.*$', r'\2 \1', i)
	if re.match(r'^([0-9\.]+)\s*([0-9]+)$',i) != None:
		i = re.sub(r'^([0-9\.]+)\s*([0-9]+)$',r'\1 \2',i)
		ip,port = i.split(' ')
		x = map(lambda x: int(x), ip.split('.') + [port])
		if x not in a:
			a += [x]
a = map(lambda i: '.'.join(map(lambda x: str(x), i[:4]))+' '+str(i[4]), sorted(a))
for i in a:
	print i
