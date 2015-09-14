#!/bin/bash
#rm done_us_tcp_ipports/* done_us_tcp_ipports_nmap/*
mkdir -p done_us_tcp
mkdir -p done_us_tcp_ipports
mkdir -p done_us_tcp_ipports_nmap
mkdir -p done_us_tcp_ipports_nmap_results
numsort_uniq="`dirname $0`/ipport-list-numsort-uniq.py"
nmap_cmds="`dirname $0`/ipport-list-to-nmap-cmds.py"
[ ! -e "$numsort_uniq" ] && { echo "$numsort_uniq script missing, aborting!" >&2 ; exit 1 ; }
[ ! -e "$nmap_cmds" ] && { echo "$nmap_cmds script missing, aborting!" >&2 ; exit 1 ; }
for i in `ls done_us_tcp`
do
	ipports="`basename $i .log`.ipports"
	if [ ! -e "done_us_tcp_ipports/$ipports" ]
	then
		python $numsort_uniq "done_us_tcp/$i" >"done_us_tcp_ipports/$ipports"
		python $nmap_cmds "done_us_tcp_ipports/$ipports" >"done_us_tcp_ipports_nmap/`basename $i .log`.sh"
		chmod +x "done_us_tcp_ipports_nmap/`basename $i .log`.sh"
	fi
done
