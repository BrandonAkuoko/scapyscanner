import socks
import socket
import pexpect
from scapy.all import *

# Set the target host and port
target_ip = "10.0.3.11" # This is one of the blue team computer ip addresses that has port 80 already open
target_port = 80

# Set the SOCKS proxy IP and port
socks_ip = "127.0.0.1"
socks_port = 9050

# Set the proxy type
socks_type = socks.SOCKS5


# Create the IP and TCP headers
ip = IP(dst=target_ip)
tcp = TCP(dport=target_port)

# Create a socket object and set the SOCKS proxy
sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
sock.set_proxy(socks_type, socks_ip, socks_port, True)

# Connect to the target host and port using the socket
sock.connect((target_ip, target_port))

# Send the SYN packet over the socket and wait for a response
response = sr1(ip/tcp, timeout=1, verbose=0, socket=sock)

# If the response is not None, the port is open
if response is not None:
    print(f"Port {target_port} is open")

else:
    print(f"Port {target_port} is closed")

# Close the socket
sock.close()
