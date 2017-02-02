#!/bin/bash

if [ "$#" -lt 2 ]
then
	echo "Usage: `basename $0` <target-ip> <delay> [ports...]" >&2
	echo "       if no ports will be provided, common ports will be used instead." >&2
	exit 1
fi
IP=$1
shift
delay=$1
shift
if [ "$#" -gt 0 ]
then
	PORTs=$@
else
	PORTs="$(`dirname $0`/common-ports.sh)"
fi
for i in $PORTs ; do
	#python nc.py $IP $i 2>&1 &
	nc -zvnw 2 $IP $i 2>&1 &
	sleep $delay
done | grep open
