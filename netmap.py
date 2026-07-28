import socket
import re 

ip_addr_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$") #expression pattern to extract the number of ports we want to scan

port_range_pattern = re.compile ("([0-9]+)-([0-9]+)") #initialising the port numbers, later on we will use variables

port_min = 0
port_max = 65535

open_ports = []

while True: #ask user for the IP address 
    ip_addr_entered = input("\n YO gang, type the IP you wanna scan rq: ")
    if ip_addr_pattern.search(ip_addr_entered):
        print(f"{ip_addr_entered} is a fr IP gang ong!!")
        break

while True:
    print("Homie now tell me port range you wanna scan in this format rq: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range fam: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid: #this can scan all 65535 ports but your computers brain will blowout as it does not use multi-threading
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

#basic socket port scanning
for port in range(port_min, port_max + 1): #connect to socket of target machine, we need the ip address and port number to connect 
    try: 
# create a socket object
# we can create a socket connection like opening a file in python
# we can change add either domain or IP address as we used socket.AF_INET and it continues with connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # we always set timer for the socket to connect to the server 
            s.connect((ip_add_entered, port)) # we used 0.5 seconds so every port it scans it allows 0.5s for a successful connection
            open_ports.append(port) # if this line runs then it was successful in connection to the port 
# we use the socket ocject we created to connect to the IP address we ip_addr_entered and the port number
# If it cannot connect, it will case exception and the open_ports list will not append the value.


    except:
        pass # we can play with this if we are interested in closed ports

for port in open_ports:
    print(f"Port {port} is open on {ip_addr_entered}.") 
# we use f string to easily format the string with variables so we don't have to do concatenation
