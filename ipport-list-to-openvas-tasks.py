#!/usr/bin/env python

'''
convert ipport list to openvas scans
'''

import sys,re
if len(sys.argv) > 2:
	filename = sys.argv[1]
else:
	sys.stderr.write('Usage: '+sys.argv[0]+' <in-file> <add|remove>\n')
	sys.exit(1)
ips = []
ports = dict()
for ip,port in map(lambda x: x.split(), filter(lambda x: re.match(r'^([0-9\.]+)\s*([0-9]+)$',x) != None, open(filename).read().strip().split('\n'))):
	if ip not in ips:
		ips += [ip]
	if ip not in ports.keys():
		ports[ip] = []
	ports[ip] += [port]	

from openvasx import Openvas
openvas = Openvas (host='localhost', port=9390, username='api', password='*****')

tag = 'project' # TODO adjust

for ip in ips:
	name = tag+'-'+ip

	tcp = ports[ip]

	if sys.argv[2] == 'add':
		print openvas.create_port_list (name=name,tcp=tcp)
		print openvas.create_target (name=name,hosts=ip,port_list_uuid=openvas.get_port_lists_uuid (name=name))
		print openvas.create_task (name=name, target=openvas.get_target_uuid (name=name), scan_config=openvas.get_scan_config_uuid (openvas.config.FULL_AND_FAST))
	if sys.argv[2] == 'remove':
		print openvas.delete_task (uuid=openvas.get_task_uuid (name=name))
		print openvas.delete_target (openvas.get_target_uuid (name=name))
		print openvas.delete_port_list (openvas.get_port_lists_uuid (name=name))
