#!/bin/bash

if [ "$#" -lt 2 ]
then
	echo "Usage: `basename $0` <retries> <pps> <target1> [target2] ..." >&2
	exit 1
fi
retries=$1
shift
pps=$1
shift
IPs=$@
for i in $IPs ; do
	if [ -e "paused.conf" ]
	then
		echo "paused.conf found. Exiting. Use \"masscan --resume paused.conf\" to resume scan or delete the file." >&2
		break
	fi
	f="${i}_mass_tcp.log"
	cmd="masscan -p1-65535 -oL $f --retries $retries --append-output --rate $pps $i"
	echo
	echo "$cmd"
	echo
	time $cmd
	cat "$f"
	[ -s "$f" ] || echo "(EMPTY)"
	echo "$f saved." >&2
done
