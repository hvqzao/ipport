#!/bin/bash
#rm done_us_tcp_ipports/* done_us_tcp_ipports_nmap/*
mkdir -p done_us_tcp
mkdir -p done_us_tcp_ipports
mkdir -p done_us_tcp_ipports_nmap
mkdir -p done_us_tcp_ipports_nmap_results
[ ! -e ipport-list-numsort-uniq.py ] && { echo "ipport-list-numsort-uniq.py script missing, aborting!" >&2 ; exit 1 ; }
[ ! -e ipport-list-to-nmap-cmds.py ] && { echo "ipport-list-to-nmap-cmds.py script missing, aborting!" >&2 ; exit 1 ; }
for i in `ls done_us_tcp`
do
	ipports="`basename $i .log`.ipports"
	if [ ! -e "done_us_tcp_ipports/$ipports" ]
	then
		python ipport-list-numsort-uniq.py "done_us_tcp/$i" >"done_us_tcp_ipports/$ipports"
		python ipport-list-to-nmap-cmds.py "done_us_tcp_ipports/$ipports" >"done_us_tcp_ipports_nmap/`basename $i .log`.sh"
		chmod +x "done_us_tcp_ipports_nmap/`basename $i .log`.sh"
	fi
done
