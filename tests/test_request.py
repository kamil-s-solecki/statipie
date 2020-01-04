import unittest
from statipie.request import parse
from statipie.request import IncorrectRequestFormatException
from statipie.request import GET, POST, PUT, DELETE, OPTIONS


class RequestTest(unittest.TestCase):
    def test_throws_exception_when_no_valid_http_method_is_provided(self):
        raw = bytes('foo', 'ascii')

        with self.assertRaises(IncorrectRequestFormatException):
            parse(raw)

    def test_recognizes_request_methods(self):
        cases = (
            (bytes('GET / HTTP/1.1', 'ascii'), GET),
            (bytes('POST / HTTP/1.1', 'ascii'), POST),
            (bytes('PUT / HTTP/1.1', 'ascii'), PUT),
            (bytes('DELETE / HTTP/1.1', 'ascii'), DELETE),
            (bytes('OPTIONS / HTTP/1.1', 'ascii'), OPTIONS),
        )
        for raw, result in cases:
            with self.subTest(raw=raw):
                r = parse(raw)

                self.assertEqual(result, r.method)

    def test_parses_uri_from_request_line(self):
        raw = bytes('GET /foo/bar HTTP/1.1', 'ascii')

        r = parse(raw)

        self.assertEqual('/foo/bar', r.uri)

    def test_parses_protocol_from_request_line(self):
        raw = bytes('GET /foo/bar HTTP/1.1', 'ascii')

        r = parse(raw)

        self.assertEqual('HTTP/1.1', r.protocol)
