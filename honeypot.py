import socket
import logging
from datetime import datetime

# Set up logging to store connection details
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def start_honeypot(host='0.0.0.0', port=9090):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"[+] Honeypot is running on {host}:{port}")
    
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"[!] Connection from {client_address}")
        
        # Log the connection details
        logging.info(f"Connection from {client_address}")
        
        # Send a response (optional)
        client_socket.send(b"Hello, you've reached a honeypot!\n")
        
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_honeypot()
