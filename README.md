# Chat Application

This is a simple Python-based chat application that allows multiple users to connect to a server and communicate with each other in real-time. The project consists of two parts: a **server** that manages client connections and broadcasts messages, and a **client** that connects to the server and allows users to send and receive messages.

## Features

- **Multiple clients:** Supports multiple clients connecting to the server simultaneously.
- **Real-time messaging:** Clients can send and receive messages in real-time.
- **Nickname-based identification:** Each client chooses a unique nickname to identify themselves in the chat.

## How It Works

1. **Server:**
   - The server listens for incoming connections on `127.0.0.1` (localhost) at port `55555`.
   - Once a client connects, the server requests a nickname and stores it.
   - It then broadcasts any received messages to all connected clients.
   
2. **Client:**
   - The client asks the user to choose a nickname and connects to the server.
   - It sends messages to the server and receives broadcasted messages from other clients.
   - The client runs two threads: one for receiving messages and one for sending messages.

## Running the Project

### 1. Start the Server:
Run the server script in one terminal:

`python server.py`

### 2. Start the Client(s):
Run the client script in separate terminals for each user (change the nickname for each client):

`python client.py`

After connecting, each client can start chatting by typing messages. The server will broadcast any message receibed from a client to all connected clients.

## Example
### Server Output:
```bash
Server is listening...
Connected with ('127.0.0.1', 12345)
Nickname of the client is Spike Spiegel
Spike Spiegel joined the chat
```
### Client Output:
```bash
Choose a nickname: Spike Spiegel
Connected to the server
Spike Spiegel: Hello, everyone!
```
