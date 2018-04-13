#!/usr/bin/env python
""" Broadcast Server Proof of Concept """
import socket

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
cs.sendto(b'This is a test', ('255.255.255.255', 31337))
