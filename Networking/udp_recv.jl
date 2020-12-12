
using Sockets

port = 8850

sock = UDPSocket()
bind(sock,ip"127.0.0.1",port)


while true
    print(String(recv(sock)))
end
	
