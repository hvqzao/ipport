#!/usr/bin/env python

name = 'us'

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	sys.stderr.write('Usage: '+sys.argv[0]+' <in-file>\n')
	sys.exit(1)
for ip in filter(lambda x: x[:1] != '#', map(lambda x: x.strip(), open(filename).read().strip().split('\n'))):
        cmd = 'us -mT -Iv '+ip+':a -r 500 -R 3'
        print 'screen -d -m -S '+name+'-'+ip+' script -f -c \''+cmd+'\' '+ip+'-'+name
