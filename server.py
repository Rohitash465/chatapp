import socket
from threading import Thread
from rich import print
from rich.panel import Panel
from datetime import datetime
from playsound import playsound

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket creating successfully")
except:
    print("An error occur when createing socket")
name = input("Enter your name:")
ip = input("Enter ip address:")
port = int(input("Enter port:"))

try:
    server.bind((ip, port))
    print("Socket bind")
except:
    print("An error occur when bind socket")

try:
    server.listen()
    print("Listening...")
except:
    print("An error occur when listen socket")

client, addr = server.accept()
with client:
    print("Connected by", addr)
    name1 = bytes(name, 'utf-8')
    client.send(name1)
    name = client.recv(1024)
    name1 = str(name, 'utf-8')
    print(name1)
    while True:
        data = input("")
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        name = '[red]You | '
        nt = name + time 
        print(Panel(data, title=nt, width=30, style='bold'))
        data1 = bytes(data, 'utf-8')
        client.send(data1)
        data = client.recv(1024)
        data1 = str(data, 'utf-8')
        #print(data1)
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print("\n")
        name = '[blue]' + name1 + ' | '
        nt = name + time
        print(Panel(data1, title=nt, width=30, style='bold'))
        playsound('recive.mp3')
