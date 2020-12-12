
import socket
import time

port = 8850

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# if hasattr(socket, "SO_REUSEPORT"):
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# sock.settimeout(0)
# sock.settimeout(0.2)
# sock.settimeout(None)

sock.bind(("", port))


while 1:

    # time.sleep(1)

    # try:
        # last_data, address = sock.recvfrom(max_size)
        print(sock.recv(1000)) # for larger timeout
    # except BlockingIOError:
    #     pass
    # except socket.timeout: # for timeout = 0
    #     pass
        


