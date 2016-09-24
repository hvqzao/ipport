#!/bin/bash

PORTs="21 22 25 53 80 88 135 139 143 389 443 445 465 514 631 993 1029 1080 1090 1098 1099 1433 1434 3128 3268 3269 3306 3389 4444 5555 5900 6000 6600 6666 7017 8000 8001 8003 8005 8009 8080 8081 8282 8443 8880 8881 8888 9000 9001 9443 9875 12721"

if [ "$#" -eq 0 ]
then
	echo "Usage: `basename $0` <target1> [target2] ..." >&2
	exit 1
fi
IPs=$@
for i in $IPs ; do
	f="${i}_mini_tcp.log"
	for j in $PORTs ; do
		#python nc.py $i $j 2>&1 &
		nc -zvnw 1 $i $j 2>&1 &
	done | sed 's/\(.\)\((UNKNOWN)\)/\1\n\2/gm' | grep open >"$f"
	cat "$f"
	[ -s "$f" ] || echo "(EMPTY)"
	echo "$f saved." >&2
done
