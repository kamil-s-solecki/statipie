def ends_with_empty_line(data):
    return data[-4:] == bytes("\r\n\r\n", "utf-8")


class Connection():
    def __init__(self, conn):
        self.conn = conn

    def send(self, response):
        self.conn.sendall(response.as_bytes())

    def read_raw_request(self):
        raw_request = bytes(0)
        while True:
            buf = self.conn.recv(1024)
            raw_request += buf
            if ends_with_empty_line(raw_request):
                break
        return raw_request
