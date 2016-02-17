#!/bin/bash
if [ "$#" -ne 2 ]
then
	echo "Usage: `basename $0` <tcp|udp> <top-n-ports>" >&2
	exit 1
fi
proto=$1
n=$2
sort -r -k3 /usr/share/nmap/nmap-services | egrep -v "^#" | grep $proto | head -$n | awk '{print $2}'
