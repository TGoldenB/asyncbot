#!/usr/bin/env python3
# simple program which terminates the Discord bot, if it is able to receive messages
# this bypasses the need for sudo
import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 7778
MESSAGE = b"terminate"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
s.close()

print("A message to terminate has been sent to the Python middle-man server.")
