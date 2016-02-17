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
	f="${i}_mass_tcp.log"
	time masscan -p1-65535 -oL "$f" --rate $pps $i
	cat "$f"
	[ -s "$f" ] || echo "(EMPTY)"
	echo "$f saved." >&2
done
