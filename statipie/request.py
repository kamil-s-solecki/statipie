GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'
OPTIONS = 'OPTIONS'

METHODS = (GET, POST, PUT, DELETE, OPTIONS,)


class IncorrectRequestFormatException(Exception):
    pass


def parse(raw_data):
    if not _has_valid_method(raw_data):
        raise IncorrectRequestFormatException

    lines = raw_data.split(bytes('\r\n', 'ascii'))

    builder = _RequestBuilder()

    builder.with_request_line(lines[0].decode('ascii'))

    return builder.build()


class Request:
    def __init__(self, method, uri, protocol):
        self._method = method
        self._uri = uri
        self._protocol = protocol

    @property
    def method(self):
        return self._method

    @property
    def uri(self):
        return self._uri

    @property
    def protocol(self):
        return self._protocol


def _has_valid_method(raw_data):
    for method in METHODS:
        if raw_data[0:len(method)] == bytes(method, 'ascii'):
            return True

    return False


class _RequestBuilder:
    def __init__(self):
        self._method = None
        self._uri = None
        self._protocol = None

    def with_request_line(self, line):
        self._method, self._uri, self._protocol = line.split(' ')

    def build(self):
        return Request(method=self._method, uri=self._uri,
                       protocol=self._protocol)
