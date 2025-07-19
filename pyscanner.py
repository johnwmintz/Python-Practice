#Using sockets to port scan
#John W. Mintz
#john.mintz@gmail.com

#pyscanner.py is a custom port scanner built in python.  This is in testing mode.
#After several ports are added it will be tested on a proving ground system.


import socket

ipaddr='127.0.0.1'#This must be changed to the target IP

#You can add more port but must create a function like the ones below for functionality.
port21=21
port22=22
port25=25
port53=53
port80=80
port443=443

#This function has been QA by JWM on 7/18/25
def sock21():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port21))
    if result == 0:
        print ("Port 21 is open")
    else:
        print ("Port 21 is not open")
    sock.close()

x21=sock21()

print (x21)


#This function has been QA by JWM on 7/18/25
def sock22():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port22))
    if result == 0:
        print ("Port 22 is open")
    else:
        print ("Port 22 is not open")
    sock.close()

x22=sock22()

print (x22)

#This function has been QA by JWM on 7/18/25
def sock25():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port25))
    if result == 0:
        print ("Port 25 is open")
    else:
        print ("Port 25 is not open")
    sock.close()

x25=sock25()

print (x25)

#This function has been QA by JWM on 7/18/25
def sock53():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port53))
    if result == 0:
        print ("Port 53 is open")
    else:
        print ("Port 53 is not open")
    sock.close()

x53=sock53()

print (x53)


#This function has been QA by JWM on 7/18/25
def sock80():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port80))
    if result == 0:
        print ("Port 80 is open")
    else:
        print ("Port 80 is not open")
    sock.close()

x80=sock80()

print (x80)


#This function has been QA by JWM on 7/18/25
def sock443():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port443))
    if result == 0:
        print ("Port 443 is open")
    else:
        print ("Port 443 is not open")
    sock.close()

x443=sock443()

print (x443)

