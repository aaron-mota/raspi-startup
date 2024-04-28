import socket
import utime as time
import network
import urequests

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

astronauts = urequests.get("http://api.open-notify.org/astros.json").json()
print(astronauts)
# {
#     "number": 7,
#     "message": "success",
#     "people": [
#         {"name": "Jasmin Moghbeli", "craft": "ISS"},
#         {"name": "Andreas Mogensen", "craft": "ISS"},
#         {"name": "Satoshi Furukawa", "craft": "ISS"},
#         {"name": "Konstantin Borisov", "craft": "ISS"},
#         {"name": "Oleg Kononenko", "craft": "ISS"},
#         {"name": "Nikolai Chub", "craft": "ISS"},
#         {"name": "Loral O'Hara", "craft": "ISS"},
#     ],
# }

for person in astronauts["people"]:
    print(f"{person['name']} is on the {person['craft']}")

wifi.disconnect()
print("Disconnected from WiFi")
print("Program complete")
