import socket
UDP_IP_ADDRESS = "20.92.112.234"
UDP_PORT_NO = 5005
Message = "Hi Toad"
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(str.encode(Message), (UDP_IP_ADDRESS, UDP_PORT_NO))
