import threading
import socket

# Localhost address (the server will run on the same machine)
host = '127.0.0.1'

# Define which port that will be used to establish the connection
port = 55555

# Create a socket object to allow IPv4, TCP connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to the specified host and port
server.bind((host, port))

# Enable the server to listen for incoming connections
server.listen()

# List to keep track of connected clients
clients = []

# List to store the nicknames of clients
nicknames = []

# Function to broadcast a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle communication with a specific client
def handle(client):
    while True:
        try:
            # Receive message from the client (up to 1024 bytes)
            message = client.recv(1024)
            # Broadcast the received message to all clients
            broadcast(message)
        except:
            # If an error occurs (e.g., client disconnects), remove them from the lists
            index = clients.index(client)
            clients.remove(client)
            client.close()
            # Get the nickname of the client that disconnected
            nickname = nicknames[index]
            # Broadcast that the client left the chat
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

# Function to accept new client connections and start a new thread for each client
def receive():
    while True:
        # Accept a new client connection
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        # Send a message to the client asking for their nickname
        client.send('NICK'.encode('ascii'))
        # Receive the client's nickname
        nickname = client.recv(1024).decode('ascii')
        # Store the client's nickname and the client object in their respective lists
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        # Broadcast that a new client has joined the chat
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        # Send a confirmation message to the client that they are connected
        client.send('Connected to the server'.encode('ascii'))

        # Start a new thread to handle this client's communication
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Start the server and begin accepting clients
print('Server is listening...')
receive()