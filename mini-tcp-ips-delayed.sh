#!/bin/bash

PORTs="$(`dirname $0`/common-ports.sh)"

if [ "$#" -eq 0 ]
then
	echo "Usage: `basename $0` <delay-secs> <target1> [target2] ..." >&2
	exit 1
fi
delay=$1
shift
IPs=$@
for i in $IPs ; do
	f="${i}_mini_tcp.log"
	for j in $PORTs ; do
		#python nc.py "$i" "$j" 2>&1 &
		nc -zvnw 2 "$i" "$j" 2>&1 &
		if [ "$delay" != "0" ]
		then
			sleep "$delay"
		fi
	done | sed 's/\(.\)\((UNKNOWN)\)/\1\n\2/gm' | grep open >"$f"
	cat "$f"
	[ -s "$f" ] || echo "(EMPTY)"
	echo "$f saved." >&2
done
