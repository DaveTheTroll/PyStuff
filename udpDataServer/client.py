import socket

msg = str.encode("Hello from client")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1.5)

sock.sendto(msg, ("192.168.213.213", 49192))
reply, address = sock.recvfrom(1000)

print(address, reply)