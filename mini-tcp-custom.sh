#!/bin/bash

if [ "$#" -lt 3 ]
then
	echo "Usage: `basename $0` <target-ip> <delay> [port1] ..." >&2
	exit 1
fi
IP=$1
shift
delay=$1
shift
PORTs=$@
for i in $PORTs ; do
	#python nc.py $IP $i 2>&1 &
	nc -zvnw 2 $IP $i 2>&1 &
	sleep $delay
done | grep open
