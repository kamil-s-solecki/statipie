import socket
import threading
from statipie.connection import Connection
from statipie import request


class ServerConfig:
    def __init__(self, port):
        self.port = port


class Server():
    def __init__(self, config, response_generator):
        self._config = config
        self._response_generator = response_generator

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(("127.0.0.1", self._config.port))
            s.listen(5)

            while True:
                conn, addr = s.accept()
                print('Connected by', addr)
                handler = self._create_connection_handler(conn)
                thread = threading.Thread(target=handler)
                thread.daemon = False
                thread.start()

    def _create_connection_handler(self, conn):
        def handler():
            with conn:
                connection = Connection(conn)
                raw_request = connection.read_raw_request()
                try:
                    req = request.parse(raw_request)
                except request.IncorrectRequestFormatException:
                    req = request.BadRequestResponse()
                resp = self._response_generator.create_from_request(req)
                connection.send(resp)
        return handler
