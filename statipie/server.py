import socket
import threading
from statipie.connection import Connection


class Server():
    def __init__(self, port):
        self.port = port

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(("127.0.0.1", self.port))
            s.listen(5)

            while True:
                conn, addr = s.accept()
                print('Connected by', addr)
                thread = threading.Thread(target=Connection(conn).handle)
                thread.daemon = False
                thread.start()
