
import socket


host = "localhost"
port = 8850


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))

sock.send(b"testing") # no guarantee its all
sock.sendall(b"magic")


while 1:
    back = sock.recv(1000)
    if back:
        print(back)


    text = input()
    sock.sendall(text.encode())
