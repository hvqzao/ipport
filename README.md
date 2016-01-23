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

Initial scans could be done using masscan or, if tester is concentrated on small subset of ports - netcat can be used. After that, detailed nmap on discovered ports is run.

Scripts also include `openvasx.py` - library for OpenVAS API handling.
`ipport-list-to-openvas-tasks.py` will use `ipport` and generate OpenVAS scans.

## License

[MIT License](https://github.com/twbs/bootstrap/blob/master/LICENSE)
