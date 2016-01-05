#!/bin/bash
#ping -c 1 $IP | grep from
if [ "$#" -eq 0 ]
then
        echo "Usage: `basename $0` <target1> [target2] ..." >&2
        echo -e "Example use:\n\tcat targets | xargs ./"`basename $0` >&2
        exit 1
fi
IPs=$@
for i in $IPs ; do
        ping -c 1 $i 2>&1 &
done | grep from | tr -d ':' | awk '{print $4}'
