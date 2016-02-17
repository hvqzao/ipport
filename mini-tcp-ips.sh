#!/bin/bash

PORTs="21 22 25 53 80 88 143 389 443 445 465 631 993 1080 1433 1434 3128 3268 3269 3389 5900 6000 8000 8001 8080 8443 9000 9001"

if [ "$#" -eq 0 ]
then
	echo "Usage: `basename $0` <target1> [target2] ..." >&2
	exit 1
fi
IPs=$@
for i in $IPs ; do
	f="${i}_mini_tcp.log"
	for j in $PORTs ; do
		nc -zvnw 1 $i $j 2>&1 &
	done | grep open >"$f"
	cat "$f"
	[ -s "$f" ] || echo "(EMPTY)"
	echo "$f saved." >&2
done
