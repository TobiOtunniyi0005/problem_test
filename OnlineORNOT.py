import socket

def is_online():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)  # 1 second timeout
        sock.sendto(b'', ('8.8.8.8', 53))  # Just try to send something
        sock.close()
        print('Online!')
        return True
    except OSError:
        return False
