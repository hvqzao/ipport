#!/bin/bash

PORTs="80 443 445 3128 3389 8000 8001 8080 8443 9000 9001"

if [ "$#" -eq 0 ]
then
       echo "Usage: `basename $0` <target1> [target2] ..." >&2
       exit 1
fi
IPs=$@
for i in $IPs ; do
       f="${i}_u_tcp.log"
       for j in $PORTs ; do
               nc -zvnw 1 $i $j 2>&1 &
       done | grep open >"$f"
       cat "$f"
       [ -s "$f" ] || echo "(EMPTY)"
       echo "$f saved." >&2
done
