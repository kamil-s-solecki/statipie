import unittest
from statipie.statics_dir import FileDoesNotExistException
from statipie.request import Request
from statipie.response import NotFoundResponse
from statipie.response import ResponseGenerator

SOME_HTML_URI = 'some_uri.html'
SOME_CSS_URI = 'some_uri.css'
SOME_BMP_URI = 'some_uri.bmp'
SOME_CONTENT = 'some file content'


class ResponseGeneratorTest(unittest.TestCase):
    def test_returns_bad_request_response_for_bad_request_format(self):
        generator = ResponseGenerator(StaticsDirMock())
        request = Request(None, None, None)

        response = generator.create_from_request(request)

        self.assertIsInstance(response, NotFoundResponse)

    def test_returns_200_response_with_file_content(self):
        statics_dir = StaticsDirMock()
        statics_dir.given_file(SOME_HTML_URI, SOME_CONTENT)
        generator = ResponseGenerator(statics_dir)
        request = Request(uri=SOME_HTML_URI, method=None, protocol=None)

        response = generator.create_from_request(request)

        self.assertEqual(response.as_bytes(), response_bytes(SOME_CONTENT))

    def test_defaults_to_index_html_file(self):
        statics_dir = StaticsDirMock()
        statics_dir.given_file('/index.html', SOME_CONTENT)
        generator = ResponseGenerator(statics_dir)
        request = Request(uri='/', method=None, protocol=None)

        response = generator.create_from_request(request)

        self.assertEqual(response.as_bytes(), response_bytes(SOME_CONTENT))

    def test_returns_200_response_with_proper_content_type(self):
        statics_dir = StaticsDirMock()
        statics_dir.given_file(SOME_CSS_URI, SOME_CONTENT)
        generator = ResponseGenerator(statics_dir)
        request = Request(uri=SOME_CSS_URI, method=None, protocol=None)

        response = generator.create_from_request(request)

        expected = response_bytes(SOME_CONTENT, mime='text/css')
        self.assertEqual(response.as_bytes(), expected)

    def test_returns_200_response_and_omits_charset_if_not_needed(self):
        statics_dir = StaticsDirMock()
        statics_dir.given_file(SOME_BMP_URI, SOME_CONTENT)
        generator = ResponseGenerator(statics_dir)
        request = Request(uri=SOME_BMP_URI, method=None, protocol=None)

        response = generator.create_from_request(request)

        expected = response_bytes(SOME_CONTENT, mime='image/bmp', charset=None)
        self.assertEqual(response.as_bytes(), expected)


class StaticsDirMock:
    def __init__(self):
        self.path_to_content = {}

    def read_bytes(self, path):
        try:
            return self.path_to_content[path]
        except KeyError:
            raise FileDoesNotExistException

    def given_file(self, path, content):
        self.path_to_content[path] = bytes(content, 'utf-8')


def response_bytes(content, mime='text/html', charset='UTF-8'):
    r = bytes()
    r += bytes('HTTP/1.0 200 OK\r\n', 'ascii')
    content_type_line = 'Content-Type: {};'.format(mime)
    if charset is not None:
        content_type_line += ' charset={}'.format(charset)
    r += bytes('{}\r\n'.format(content_type_line), 'ascii')
    r += bytes('\r\n', 'ascii')
    r += bytes(content, 'utf-8')
    r += bytes('\r\n', 'ascii')
    r += bytes('\r\n', 'ascii')
    return r
