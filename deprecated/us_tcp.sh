#!/bin/bash

hosts="int" # file with hosts to scan (use # to comment out entries)
pps=300 # packets per second
#repeat=3 # repeats of packets

#echo "Unicorn / masscan will quickly find open TCP ports on all hosts:"
for i in `cat $hosts | egrep -v "^\s*#"` ; do
	#time script -f -c "unicornscan -mT -Iv -r $pps -R $repeat $i:a" us_tcp_$i.log
	time script -f -c "masscan -p1-65535 --rate $pps $i" us_tcp_$i.log
done
