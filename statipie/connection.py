from statipie import request
from statipie import response


def ends_with_empty_line(data):
    return data[-4:] == bytes("\r\n\r\n", "utf-8")


class Connection():
    def __init__(self, conn):
        self.conn = conn

    def handle(self):
        with self.conn:
            raw_request = self._read_raw_request()
            req = request.Request(raw_request)
            resp = response.create_from_request(request)
            self.conn.sendall(resp.as_bytes())

    def _read_raw_request(self):
        raw_request = bytes(0)
        while True:
            buf = self.conn.recv(1024)
            raw_request += buf
            if ends_with_empty_line(raw_request):
                break
        return raw_request
