import socket

reply = str.encode("HELLO VIA THING")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 49192))

while True:
    msg, address = sock.recvfrom(100)
    print(address, msg)
    sock.sendto(reply, address)