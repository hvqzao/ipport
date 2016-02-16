#!/bin/bash

if [ "$#" -lt 3 ]
then
	echo "Usage: `basename $0` <top-n-ports> <pps> <target1> [target2] ..." >&2
	exit 1
fi
n=$1
shift
pps=$1
shift
IPs=$@

# top n udp ports
top_ports=`sort -r -k3 /usr/share/nmap/nmap-services | egrep -v "^#" | grep udp | head -$n | awk '{print $2}' | awk -F/ '{print "U:"$1}' | xargs echo -n | tr ' ' ','`

for i in $IPs ; do
	time masscan -p$top_ports -oL ${i}_masscan_udp_${n}.log --rate $pps $i
done
cat ${i}_masscan_udp_${n}.log
