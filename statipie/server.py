import socket
import threading
from statipie.connection import Connection
from statipie import response
from statipie import request


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
                handler = _create_connection_handler(conn)
                thread = threading.Thread(target=handler)
                thread.daemon = False
                thread.start()


def _create_connection_handler(conn):
    def handler():
        with conn:
            connection = Connection(conn)
            raw_request = connection.read_raw_request()
            req = request.parse(raw_request)
            resp = response.create_from_request(req)
            connection.send(resp)
    return handler
