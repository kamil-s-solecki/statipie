from statipie.statics_dir import FileDoesNotExistException


class ResponseGenerator:
    def __init__(self, statics_dir):
        self._statics_dir = statics_dir

    def create_from_request(self, request):
        try:
            body = self._statics_dir.read_bytes(request.uri)
            res = Response(body)
        except FileDoesNotExistException:
            res = NotFoundResponse()

        return res


class Response:
    def __init__(self, body, code=200, message='OK'):
        self._body = body
        self._code = code
        self._message = message

    def as_bytes(self):
        response = bytes()
        status_line = 'HTTP/1.0 {} {}\r\n'.format(self._code, self._message)
        response += bytes(status_line, 'ascii')
        response += bytes('Content-Type: text/html; charset=UTF-8\r\n',
                          'ascii')
        response += bytes('\r\n', 'ascii')
        response += self._body
        response += bytes('\r\n', 'ascii')
        response += bytes('\r\n', 'ascii')
        return response


class BadRequestResponse(Response):
    def __init__(self):
        body = bytes('<h1>Bad Request</h1>\r\n', 'utf-8')
        super().__init__(body, 400, 'Bad Request')


class NotFoundResponse(Response):
    def __init__(self):
        body = bytes('<h1>Not Found</h1>\r\n', 'utf-8')
        super().__init__(body, 404, 'Not Found')
