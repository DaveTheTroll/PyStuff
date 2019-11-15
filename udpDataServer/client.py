import socket

msg = str.encode("Hello from client")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.5)

sock.sendto(msg, ("127.0.0.1", 49192))
reply, address = sock.recvfrom(1000)

print(reply, address)