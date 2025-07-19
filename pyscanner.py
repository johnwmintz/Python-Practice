#Using sockets to port scan
#John W. Mintz
#john.mintz@gmail.com

#pyscanner.py is a custom port scanner built in python.  This is in testing mode.
#After several ports are added it will be tested on a proving ground system.


import socket

ipaddr='127.0.0.1'#This must be changed to the target IP

#port variables
#You can add more port but must create a function like the ones below for functionality.
port21=21 #added 7/18/25 with function
port22=22 #added 7/18/25 with function
port25=25 #added 7/18/25 with function
port53=53 #added 7/18/25 with function
port80=80 #added 7/18/25 with function
port88=88
port135=135
port139=139
port389=389
port443=443 #added 7/18/25 with function
port445=445
port464=464
port593=593
port636=636
port3268=3268
port3269=3269
port5985=5985
port9389=9389

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

