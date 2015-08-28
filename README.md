# ipport: Infrastructure recon / rapid port scanning helpers

Small subset of Bash/Python scripts which could be used for fast TCP scanning.
Most of them work on `ipport` lists, i.e.
```
IP1 PORT1
IP1 PORT2
IP2 PORT1
IP3 PORT3
...
```
For some scripts `ipport` is output, for other it is input.

Initial scans could be done using unicornscan or, if tester is concentrated on small subset of ports - netcat can be used. 

Scripts also include `openvasx.py` - library for OpenVAS API handling.
`ipport-list-to-openvas-tasks.py` will use `ipport` and generate OpenVAS scans.

Having only IP list and targeting all TCP port, simplest approach would be to use:

`us_tcp.sh` will process defined input file and run unicornscan. Results must be manually put to `us_tcp_done` folder.

`us_tcp_ipports.sh` will generate ipport lists based on previous command result and right after - nmap scan commands only for found ports.

`us_tcp_ipports_nmap.sh` will issue nmap scans for which there are no results yet in final `done_us_tcp_ipports_nmap_results` folder.

## License

[MIT License](https://github.com/twbs/bootstrap/blob/master/LICENSE)
