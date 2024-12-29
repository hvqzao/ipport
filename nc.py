#!/usr/bin/env python

import socket, sys

targetIP = sys.argv[1]
i = int(sys.argv[2])

socket_timeout = 2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(socket_timeout)
result = s.connect_ex((targetIP, i))
if(result == 0) :
    print(targetIP, i, "open")
s.close()
