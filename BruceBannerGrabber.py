import socket
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

socket.setdefaulttimeout(1) #Default timeout

clear()

if os.name == 'nt':
    os.system("color 0a")

def banner():
    print("____                                   ")
    print("|  _ \                                  ")
    print("| |_) |_ __ _   _  ___ ___              ")
    print("|  _ <| '__| | | |/ __/ _ \             ")
    print("| |_) | |  | |_| | (_|  __/             ")
    print("|____/|_|   \__,_|\___\___|             ")
    print("|  _ \                                  ")
    print("| |_) | __ _ _ __  _ __   ___ _ __      ")
    print("|  _ < / _` | '_ \| '_ \ / _ \ '__|     ")
    print("| |_) | (_| | | | | | | |  __/ |        ")
    print("|____/_\__,_|_| |_|_| |_|\___|_|        ")
    print(" / ____|         | |   | |              ")
    print("| |  __ _ __ __ _| |__ | |__   ___ _ __ ")
    print("| | |_ | '__/ _` | '_ \| '_ \ / _ \ '__|")
    print("| |__| | | | (_| | |_) | |_) |  __/ |   ")
    print(" \_____|_|  \__,_|_.__/|_.__/ \___|_|   ")
                                         
banner() 
print("")                             
host = input("Enter Hostname: ") 

host_valid = False
clear()

while not host_valid:
    try:
        print("Checking Host...")
        ip_address = socket.gethostbyname(host)
        host_valid = True
    except:
        clear()
        print("Invalid Host, please try again.")
        print("")
        host = input("Please Enter A Hostname: ")

clear()
banner()
print("")
print(f"Valid host name, IP address is {ip_address}")
print("")
port = int(input("Enter the starting port number: "))
print("")
porte = int(input("Enter the ending port number: "))
porte += 1
clear()
print("Bruce Banner Grabber: ")
print("-------------------------------------------------")
while port != porte:

    try:
        my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Socket created using AFINET address familing using IPV4 w/ TCP
        my_socket.connect((ip_address, port))
        message = ''

        if port == 80: #If the port is 80 send a new message for more information
            message = 'GET / HTTP/1.1\r\nHost: ' + str(ip_address) + '\r\n\r\n'

        message = message.encode('utf-8')
        my_socket.sendall(message)
        
        return_data = my_socket.recv(10000).decode('utf-8', 'ignore') #Ignore is to ignore any characters the code can't understand.
        return_data_len = len(return_data)
        print(f"Port {port :d} is Open")
        print("")
        if return_data_len > 2:
            print(f"Banner information returned is: \n{return_data :s}\n-------------------------------------------------")
        else:
            print("Bruce Could Not Grab The Banner\n\n-------------------------------------------------")
        my_socket.close()
    except socket.error as e:
        pass
    port += 1

print('')
print("Banner Grabbing complete!")
print("")
input("Press Enter To Exit")