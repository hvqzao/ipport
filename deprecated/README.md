# deprecated

Unmaintained scripts land here.

One script parsing to nmap scan is sufficient.

## unicornscan route

Having only IP list and targeting all TCP port, simplest approach would be to use:

`us_tcp.sh` will process defined input file and run unicornscan. Results must be manually put to `us_tcp_done` folder.

`us_tcp_ipports.sh` will generate ipport lists based on previous command result and right after - nmap scan commands only for found ports.

`us_tcp_ipports_nmap.sh` will issue nmap scans for which there are no results yet in final `done_us_tcp_ipports_nmap_results` folder.

