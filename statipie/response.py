import os
from statipie.statics_dir import FileDoesNotExistException
from statipie.mime import create_from_extension as create_mime_from_extension


class ResponseGenerator:
    def __init__(self, statics_dir):
        self._statics_dir = statics_dir

    def create_from_request(self, request):
        try:
            path = '/index.html' if '/' == request.uri else request.uri
            body = self._statics_dir.read_bytes(path)
            headers = self._create_headers(path)
            res = Response(body, headers=headers)
        except FileDoesNotExistException:
            res = NotFoundResponse()

        return res

    def _create_headers(self, path):
        return [self._content_type_header(path)]

    def _content_type_header(self, path):
        _, ext = os.path.splitext(path)
        mime = create_mime_from_extension(ext)

        if mime.charset is not None:
            val = '{}; charset={}'.format(mime.type, mime.charset)
        else:
            val = '{};'.format(mime.type)

        return Header('Content-Type', val)


class Response:
    def __init__(self, body, code=200, message='OK', headers=[]):
        self._body = body
        self._code = code
        self._message = message
        self._headers = headers

    def as_bytes(self):
        response = bytes()
        status_line = 'HTTP/1.0 {} {}\r\n'.format(self._code, self._message)
        response += bytes(status_line, 'ascii')
        for h in self._headers:
            response += bytes('{}: {}\r\n'.format(h.name, h.value),
                              'ascii')
        response += bytes('\r\n', 'ascii')
        response += self._body
        response += bytes('\r\n', 'ascii')
        response += bytes('\r\n', 'ascii')
        return response


class Header:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class BadRequestResponse(Response):
    def __init__(self):
        body = bytes('<h1>Bad Request</h1>\r\n', 'utf-8')
        super().__init__(body, 400, 'Bad Request')


class NotFoundResponse(Response):
    def __init__(self):
        body = bytes('<h1>Not Found</h1>\r\n', 'utf-8')
        super().__init__(body, 404, 'Not Found')
