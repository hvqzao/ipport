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
	if [ -e "paused.conf" ]
	then
		echo "paused.conf found. Exiting." >&2
		break
	fi
	f="${i}_mass_tcp.log"
	time masscan -p1-65535 -oL "$f" --append-output --rate $pps $i
	cat "$f"
	[ -s "$f" ] || echo "(EMPTY)"
	echo "$f saved." >&2
done
