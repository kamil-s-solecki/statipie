class Connection():
    def __init__(self, conn):
        self.conn = conn

    def handle(self):
        with self.conn:
            while True:
                data = self.conn.recv(1024)
                if not data:
                    break
                self.conn.sendall(data)
