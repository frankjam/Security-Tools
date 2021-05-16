import socket
target_ip='127.0.0.1'


def port_scann(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(target_ip,port)
        return True
    except:
        return False
    

for port in range(0,65535):
    result = port_scann(port)
    if result:
        print("port {} is open".format(port))
    else:
        print("port {} is closed".format(port))
