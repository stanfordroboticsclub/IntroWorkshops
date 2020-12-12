
import socket

import json
import time


target = "127.0.0.1"
port = 8850

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.connect( (target, port))

while 1:
    line = input()

    # time.sleep(1)
    # sock.send("test")


    sock.send( json.dumps({"mesg": line}).encode() )

sock.close()

# b"abcde".decode("utf-8")
# "test".encode('utf-8')

# json.dumps([1,2,3]).encode()
# json.loads("[1,2,3]")
