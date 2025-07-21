#Using sockets to port scan
#John W. Mintz
#john.mintz@gmail.com

#pyscanner.py is a custom port scanner built in python.  This is in testing mode.
#After several ports are added it will be tested on a proving ground system.


import socket
import sys

ipaddr='127.0.0.1'#This has to be changed before running scan

#port variables
#You can add more port but must create a function like the ones below for functionality.
port21=21 #added 7/18/25 with function
port22=22 #added 7/18/25 with function
port25=25 #added 7/18/25 with function
port53=53 #added 7/18/25 with function
port80=80 #added 7/18/25 with function
port88=88 #added 7/19/25 with function
port135=135 #added 7/19/25 with function
port139=139 #added 7/19/25 with function
port389=389 #added 7/20/25 with function
port443=443 #added 7/18/25 with function
port445=445 #added 7/20/25 with function
port464=464 #added 7/20/25 with function
port593=593 #added 7/20/25 with function
port636=636 #added 7/20/25 with function
port3268=3268
port3269=3269
port5985=5985
port9389=9389

#This function has been QA by JWM on 7/18/25
def sock21():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port21))
    if result == 0:
        print ("Port 21 open")
    else:
        print ("Port 21 closed")
    sock.close()

x21=sock21()




#This function has been QA by JWM on 7/18/25
def sock22():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port22))
    if result == 0:
        print ("Port 22 open")
    else:
        print ("Port 22 closed")
    sock.close()

x22=sock22()



#This function has been QA by JWM on 7/18/25
def sock25():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port25))
    if result == 0:
        print ("Port 25 open")
    else:
        print ("Port 25 closed")
    sock.close()

x25=sock25()



#This function has been QA by JWM on 7/18/25
def sock53():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port53))
    if result == 0:
        print ("Port 53 open")
    else:
        print ("Port 53 closed")
    sock.close()

x53=sock53()




#This function has been QA by JWM on 7/18/25
def sock80():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port80))
    if result == 0:
        print ("Port 80 open")
    else:
        print ("Port 80 closed")
    sock.close()

x80=sock80()



def sock88():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port88))
    if result == 0:
        print ("Port 88 open")
    else:
        print ("Port 88 closed")
    sock.close()

x88=sock88()




def sock135():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port135))
    if result == 0:
        print ("Port 135 open")
    else:
        print ("Port 135 closed")
    sock.close()

x135=sock135()




def sock139():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port139))
    if result == 0:
        print ("Port 139 open")
    else:
        print ("Port 139 closed")
    sock.close()

x139=sock139()

def sock389():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port389))
    if result == 0:
        print ("Port 389 open")
    else:
        print ("Port 389 closed")
    sock.close()

x389=sock389()






#This function has been QA by JWM on 7/18/25
def sock443():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port443))
    if result == 0:
        print ("Port 443 open")
    else:
        print ("Port 443 closed")
    sock.close()

x443=sock443()


def sock445():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port445))
    if result == 0:
        print ("Port 445 open")
    else:
        print ("Port 445 closed")
    sock.close()

x445=sock445()


def sock464():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port464))
    if result == 0:
        print ("Port 464 open")
    else:
        print ("Port 464 closed")
    sock.close()

x464=sock464()


def sock593():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port593))
    if result == 0:
        print ("Port 593 open")
    else:
        print ("Port 593 closed")
    sock.close()

x593=sock593()




def sock636():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port636))
    if result == 0:
        print ("Port 636 open")
    else:
        print ("Port 636 closed")
    sock.close()

x636=sock636()


