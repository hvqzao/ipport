#!/bin/bash

for i in `ls done_us_tcp_ipports_nmap`
do
	log="`basename $i .sh`_nmap.log"
	if [ ! -e "done_us_tcp_ipports_nmap_results/$log" ]
	then
		
		if [ `cat "done_us_tcp_ipports_nmap/$i" | wc -l` -ne 0 ]
		then
			echo
			echo "done_us_tcp_ipports_nmap/$i"
			#echo "Press Enter to continue..."
			#read
			"./done_us_tcp_ipports_nmap/$i"
		fi
	fi
done
