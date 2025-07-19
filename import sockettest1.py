import socket

ipaddr='127.0.0.1'
port21=21
port22=22
port25=25
port53=53
port80=80
port443=443

def sock21():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port21))
    if result == 0:
        print ("Port is open")
    else:
        print ("{port21} is not open")
    sock.close()

x21=sock21()

print (x21)



def sock80():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipaddr,port80))
    if result == 0:
        print ("Port is open")
    else:
        print ("Port is not open")
    sock.close()

x80=sock80()

print (x80)

