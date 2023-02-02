import json

# Load the JSON file into a variable
with open('TableCastWebsitePHP/data.json') as json_file:
    data = json.load(json_file)

line1 = "ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev"
line2 = "update_config=1"
line3 = "country=AT"
line4 = "network={"
line5 = "ssid=\""
line6 = "psk=\""
line7 = "key_mgmt=WPA-PSK"
line8 = "}"

string = str(data)
print(string)

string = string.replace('[', '')
string = string.replace(']', '')

data = eval(string)

f=open("TableCastWebsitePHP/wpa_supplicant.conf", "w")

line5 = line5 + data['Wlanname'] + "\""
line6 = line6 + data['Wlanpasswort'] + "\""

f.write(line1 + "\n")
f.write(line2 + "\n")
f.write(line3 + "\n")
f.write(line4 + "\n")
f.write(line5 + "\n")
f.write(line6 + "\n")
f.write(line7 + "\n")
f.write(line8 + "\n")

#print(string)
# Access individual variables from the JSON file
print(data['Helligkeit'])
print(data['Geschwindigkeit'])
print(data['Text'])