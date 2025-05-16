import threading
import socket

# Ask the user to choose a nickname for the chat
nickname = input('Choose a nickname: ')

# Create a socket object to connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at localhost (127.0.0.1) on port 55555
client.connect(('127.0.0.1', 55555))

# Function to receive messages from the server
def receive():
    while True:
        try:
            # Receive a message from the server (up to 1024 bytes)
            message = client.recv(1024).decode('ascii')
            
            # If the server sends 'NICK', send the chosen nickname back
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                # Print any other messages from the server (e.g., chat messages)
                print(message)
        except:
            # Handle errors (e.g., if the server disconnects)
            print("An error has occurred")
            client.close()
            break

# Function to send messages to the server
def write():
    while True:
        # Get the user's input, prepend the nickname, and send to the server
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Start a thread to allow the user to write and send messages
write_thread = threading.Thread(target=write)
write_thread.start()