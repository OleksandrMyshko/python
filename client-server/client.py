import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 5555))
    s = 'Hello, server'
    sock.send(s.encode())

    answer = sock.recv(1024).decode()
    print(answer)

    sock.close()


main()