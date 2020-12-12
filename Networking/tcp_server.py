
import socket



host = '127.0.0.1'
port = 8850

sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()



conn, addr = sock.accept()

print('Connected by', addr)
while True:
    data = conn.recv(10)
    if data:
        print(data)
        conn.sendall(b"echo")
        conn.sendall(data)
