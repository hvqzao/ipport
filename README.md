# ipport: Infrastructure recon / rapid port scanning

Small subset of Bash/Python scripts which could be used for fast TCP and UDP scanning.
Most of them work on `ipport` files, which are either tcp or udp port lists, i.e.
```
IP1 PORT1
IP1 PORT2
IP2 PORT1
IP3 PORT3
...
```
For some scripts `ipport` is output, for other it is input.

Initial scans could be done using masscan or, if tester is concentrated on small subset of ports - netcat can be used. After that, detailed nmap on discovered ports is run.

## Mini scan (really quick scan)

```sh
root@kali:~/x/t/demo# ~/x/p/ipport/mini-tcp-ips.sh 
Usage: mini-tcp-ips.sh <target1> [target2] ...
```
```sh
root@kali:~/x/t/demo# time ~/x/p/ipport/mini-tcp-ips.sh 192.168.43.137
(UNKNOWN) [192.168.43.137] 80 (http) open
(UNKNOWN) [192.168.43.137] 21 (ftp) open
(UNKNOWN) [192.168.43.137] 53 (domain) open
(UNKNOWN) [192.168.43.137] 6000 (x11) open
(UNKNOWN) [192.168.43.137] 22 (ssh) open
(UNKNOWN) [192.168.43.137] 5900 (?) open
(UNKNOWN) [192.168.43.137] 25 (smtp) open
(UNKNOWN) [192.168.43.137] 445 (microsoft-ds) open
192.168.43.137_mini_tcp.log saved.

real	0m0.048s
user	0m0.000s
sys	0m0.032s
```

## Parsing output to ipport (works for mini, mass tcp or udp)

```sh
root@kali:~/x/t/demo# ~/x/p/ipport/to-ipport-parse-numsort-uniq.py
Usage: /root/x/p/ipport/to-ipport-parse-numsort-uniq.py <in-file>
```
```sh
root@kali:~/x/t/demo# ~/x/p/ipport/to-ipport-parse-numsort-uniq.py 192.168.43.137_mini_tcp.log 
192.168.43.137_mini_tcp_ipport.log saved.
```

## Parsing ipport to nmap scan and actual scanning

```sh
root@kali:~/x/t/demo# ~/x/p/ipport/ipport-to-nmap-tcp.py 
Usage: /root/x/p/ipport/ipport-to-nmap-tcp.py <tag> <in-file>
```
```sh
root@kali:~/x/t/demo# ~/x/p/ipport/ipport-to-nmap-tcp.py mini 192.168.43.137_mini_tcp_ipport.log 
script -f -c "nmap -Pn -vv -sT -A --version-all -p 21,22,25,53,80,445,5900,6000 -oA .192.168.43.137_mini_nmap_tcp 192.168.43.137" 192.168.43.137_mini_nmap_tcp.log
```
```sh
root@kali:~/x/t/demo# ~/x/p/ipport/ipport-to-nmap-tcp.py mini 192.168.43.137_mini_tcp_ipport.log | bash
Script started, file is 192.168.43.137_mini_nmap_tcp.log

Starting Nmap 7.01 ( https://nmap.org ) at 2016-02-17 22:57 CET
NSE: Loaded 132 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 22:57
[...]
```

## Masscan tcp

(Both tcp and udp masscan can be resumed in case you need to interrupt them for some reason)

```sh
root@kali:~/x/t/demo# ~/x/p/ipport/mass-tcp-ips.sh 
Usage: mass-tcp-ips.sh <pps> <target1> [target2] ...
```
```sh
root@kali:~/x/t/demo# ~/x/p/ipport/mass-tcp-ips.sh 500 192.168.43.137

Starting masscan 1.0.3 (http://bit.ly/14GZzcT) at 2016-02-17 21:59:51 GMT
 -- forced options: -sS -Pn -n --randomize-hosts -v --send-eth
Initiating SYN Stealth Scan
Scanning 1 hosts [65535 ports/host]
[...]
```
```sh
root@kali:~/x/t/demo# ~/x/p/ipport/to-ipport-parse-numsort-uniq.py 192.168.43.137_mass_tcp.log 
192.168.43.137_mass_tcp_ipport.log saved.
```
```sh
root@kali:~/x/t/demo# ~/x/p/ipport/ipport-to-nmap-tcp.py mass 192.168.43.137_mass_tcp_ipport.log 
script -f -c "nmap -Pn -vv -sT -A --version-all -p 21,22,23,25,53,80,111,139,445,512,513,514,1099,1524,2049,2121,3306,3632,5432,5900,6000,6667,6697,8009,8180,8787,33181,33667,34663,49129 -oA .192.168.43.137_mass_nmap_tcp 192.168.43.137" 192.168.43.137_mass_nmap_tcp.log
```

## Masscan udp

```sh
root@kali:~/x/t/demo# ~/x/p/ipport/mass-udp-ips.sh
Usage: mass-udp-ips.sh <top-n-ports> <pps> <target1> [target2] ...
```
```sh
root@kali:~/x/t/demo# ~/x/p/ipport/mass-udp-ips.sh 1000 500 192.168.43.137

Starting masscan 1.0.3 (http://bit.ly/14GZzcT) at 2016-02-17 22:01:22 GMT
 -- forced options: -sS -Pn -n --randomize-hosts -v --send-eth
Initiating SYN Stealth Scan
Scanning 1 hosts [1000 ports/host]
[...]
```
```sh
root@kali:~/x/t/demo# ~/x/p/ipport/to-ipport-parse-numsort-uniq.py 192.168.43.137_mass_udp_1000.log 
192.168.43.137_mass_udp_1000_ipport.log saved.
```
```sh
root@kali:~/x/t/demo# ~/x/p/ipport/ipport-to-nmap-udp.py mass_1000 192.168.43.137_mass_udp_1000_ipport.log 
script -f -c "nmap -Pn -vv -sU -A --version-all -p 53,137 -oA .192.168.43.137_mass_1000_nmap_udp 192.168.43.137" 192.168.43.137_mass_1000_nmap_udp.log
```

## Example results

```sh
-rw-r--r--  1 root root   476 Feb 17 23:20 .192.168.43.137_mass_1000_nmap_udp.gnmap
-rw-r--r--  1 root root  3833 Feb 17 23:20 192.168.43.137_mass_1000_nmap_udp.log
-rw-r--r--  1 root root  2096 Feb 17 23:20 .192.168.43.137_mass_1000_nmap_udp.nmap
-rw-r--r--  1 root root  5572 Feb 17 23:20 .192.168.43.137_mass_1000_nmap_udp.xml
-rw-r--r--  1 root root  2082 Feb 17 23:17 .192.168.43.137_mass_nmap_tcp.gnmap
-rw-r--r--  1 root root 12886 Feb 17 23:17 192.168.43.137_mass_nmap_tcp.log
-rw-r--r--  1 root root  9805 Feb 17 23:17 .192.168.43.137_mass_nmap_tcp.nmap
-rw-r--r--  1 root root 25553 Feb 17 23:17 .192.168.43.137_mass_nmap_tcp.xml
-rw-r--r--  1 root root   616 Feb 17 23:13 192.168.43.137_mass_tcp_ipport.log
-rw-r--r--  1 root root  1231 Feb 17 23:13 192.168.43.137_mass_tcp.log
-rw-r--r--  1 root root    39 Feb 17 23:19 192.168.43.137_mass_udp_1000_ipport.log
-rw-r--r--  1 root root    94 Feb 17 23:18 192.168.43.137_mass_udp_1000.log
-rw-r--r--  1 root root   852 Feb 17 23:11 .192.168.43.137_mini_nmap_tcp.gnmap
-rw-r--r--  1 root root  9397 Feb 17 23:11 192.168.43.137_mini_nmap_tcp.log
-rw-r--r--  1 root root  7361 Feb 17 23:11 .192.168.43.137_mini_nmap_tcp.nmap
-rw-r--r--  1 root root 17232 Feb 17 23:11 .192.168.43.137_mini_nmap_tcp.xml
-rw-r--r--  1 root root   157 Feb 17 23:10 192.168.43.137_mini_tcp_ipport.log
-rw-r--r--  1 root root   353 Feb 17 23:10 192.168.43.137_mini_tcp.log
```

## top ports

Someone might find it useful.

```sh
root@kali:~/x/t/demo# ~/x/p/ipport/top-ports.sh 
Usage: top-ports.sh <tcp|udp> <top-n-ports>
```
```sh
root@kali:~/x/t/demo# ~/x/p/ipport/top-ports.sh tcp 10
80/tcp
23/tcp
443/tcp
21/tcp
22/tcp
25/tcp
3389/tcp
110/tcp
445/tcp
139/tcp
```

## openvasx

Scripts also include `openvasx.py` - library for OpenVAS API handling.
`ipport-list-to-openvas-tasks.py` will use `ipport` and generate OpenVAS scans.

## License

[MIT License](https://github.com/twbs/bootstrap/blob/master/LICENSE)
