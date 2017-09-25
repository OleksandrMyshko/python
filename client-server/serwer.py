import socket
import threading

class Client_handler(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        massage = self.sock.recv(1024).decode()
        massage += '!'
        self.sock.send(massage.encode())
        self.sock.close()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 5555))
    sock.listen(5)
    while True:
        client_socket, addr = sock.accept()
        hendler = Client_handler(client_socket)
        hendler.start()

    sock.close()


main()