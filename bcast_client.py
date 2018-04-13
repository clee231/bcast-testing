#!/usr/bin/env python
""" Broadcast Client Proof of Concept """
import socket

sock_inst = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_inst.bind(('',31337))
mesg = sock_inst.recvfrom(1024)
print (mesg[0])
