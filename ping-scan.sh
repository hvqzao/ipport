#!/bin/bash
#ping -c 1 $IP | grep from
if [ "$#" -eq 0 ]
then
        echo "Usage: `basename $0` <count> <target1> [target2] ..." >&2
        echo -e "Example use:\n\tcat targets | xargs ./"`basename $0` >&2
        exit 1
fi
count=$1
shift
IPs=$@
for i in $IPs ; do
        ping -c $count $i 2>&1 &
done | grep from | tr -d ':' | awk '{print $4}' | sort -u
