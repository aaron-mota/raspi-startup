import socket

## NOTE: THIS FILE IS AN EXAMPLE OF A CLIENT THAT CAN COMMUNICATE WITH THE WIFI-SERVER ON THE PICO (main.py)

# Set up client
serverIpAddress = "192.168.1.18"  # may need update this (or make as reserved IP in router (aka static IP))
SERVER_PORT = 2222
BUFFER_SIZE = 1024

# Create client socket
serverIpAddress = (serverIpAddress, SERVER_PORT)
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create messages (to send to server)
while True:
    command = input("What is your command? ")
    commandEncoded = command.encode("utf-8")

    # Send messages (to server)
    UDPClientSocket.sendto(commandEncoded, serverIpAddress)

    # # Receive messages (from server)
    serverMessage, serverIpAddressAndPortFromMessage = UDPClientSocket.recvfrom(BUFFER_SIZE)
    # msg = "Message from Server: {}".format(msgFromServer[0])
    msgFromServerDecoded = serverMessage.decode("utf-8")
    print("MESSAGE RECEIVED (FROM SERVER): ", msgFromServerDecoded)
    print("FROM SERVER IP: ", serverIpAddressAndPortFromMessage)
