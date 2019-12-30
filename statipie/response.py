def create_from_request(request):
    return Response()


class Response:
    def as_bytes(self):
        response = ''
        response += 'HTTP/1.0 400 Bad Request\r\n'
        response += 'Content-Type: text/html; charset=UTF-8\r\n'
        response += '\r\n'
        response += '<h1>Bad request</h1>\r\n'
        response += '\r\n'
        return bytes(response, 'utf-8')
