import socket
import utime as time
import network

# CONNECT TO WIFI
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

WIFI_SSID = "NETGEAR43"
WIFI_PASSWORD = "cloudyocean088"
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

while not wifi.isconnected():
    print("Connecting to WiFi...")
    time.sleep(1)
print("Connected to WiFi")

try:
    # WIFI CONFIG
    wifiInfo = wifi.ifconfig()
    serverIpAddress = wifiInfo[0]  # may need update this (or make as reserved IP in router (aka static IP))
    print("IP Address (server): ", wifiInfo[0])
    print("UDP Server Up and Waiting...")
    SERVER_PORT = 2222  # can be whatever port you want
    BUFFER_SIZE = 1024  # bytes
    UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPServerSocket.bind((serverIpAddress, SERVER_PORT))

    # RECEIVE MESSAGES
    while True:
        clientMessage, clientIpAddress = UDPServerSocket.recvfrom(BUFFER_SIZE)
        messageDecoded = clientMessage.decode("utf-8")
        print("MESSAGE RECEIVED: ", messageDecoded)
        print("FROM: ", clientIpAddress[0])

        dataString = "Message received: " + messageDecoded
        dataStringEncoded = dataString.encode("utf-8")
        UDPServerSocket.sendto(dataStringEncoded, clientIpAddress)

except KeyboardInterrupt:
    print("Closing socket...")
    UDPServerSocket.close()
    print("Socket closed")
    wifi.disconnect()
    print("Disconnected from WiFi")
    print("Program complete")
except Exception as e:
    print("Error: ", e)
finally:
    print("Closing socket...")
    UDPServerSocket.close()
    print("Socket closed")
    wifi.disconnect()
    print("Disconnected from WiFi")
    print("Program complete")
