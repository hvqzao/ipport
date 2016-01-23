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
	time script -f -c "masscan -p1-65535 --rate $pps $i" $i"_masscan_tcp.log"
done
