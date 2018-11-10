#!/bin/bash

PORTs="$(`dirname $0`/common-ports.sh)"

if [ "$#" -eq 0 ]
then
	echo "Usage: `basename $0` <target1> [target2] ..." >&2
	exit 1
fi
IPs=$@
for i in $IPs ; do
	f="${i}_mini_tcp.log"
	for j in $PORTs ; do
		#python nc.py "$i" "$j" 2>&1 &
		nc -zvnw 2 "$i" "$j" 2>&1 &
	done | sed 's/\(.\)\((UNKNOWN)\)/\1\n\2/gm' | egrep "(open|Connected)" >"$f"
	cat "$f"
	[ -s "$f" ] || echo "(EMPTY)"
	echo "$f saved." >&2
done
