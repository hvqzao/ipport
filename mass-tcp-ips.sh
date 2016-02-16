#!/bin/bash

if [ "$#" -lt 2 ]
then
	echo "Usage: `basename $0` <pps> <target1> [target2] ..." >&2
	exit 1
fi
pps=$1
shift
IPs=$@
for i in $IPs ; do
	time masscan -p1-65535 -oL ${i}_masscan_tcp.log --rate $pps $i
done
cat ${i}_masscan_tcp.log
