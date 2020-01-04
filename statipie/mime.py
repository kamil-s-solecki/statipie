# types:
TEXT_HTML = 'text/html'
TEXT_CSS = 'text/css'

APPLICATION_JAVASCRIPT = 'application/javascript'

IMAGE_BMP = 'image/bmp'
IMAGE_PNG = 'image/png'

# charsets
UTF_8 = 'UTF-8'


_mimes_by_ext = {
    '.html': (TEXT_HTML, UTF_8),
    '.css': (TEXT_CSS, UTF_8),

    '.js': (APPLICATION_JAVASCRIPT, UTF_8),

    '.bmp': (IMAGE_BMP, None),
    '.png': (IMAGE_PNG, None),
}


def create_from_extension(ext):
    t, c = _mimes_by_ext[ext]
    return Mime(t, charset=c)


class Mime:
    def __init__(self, _type, charset=None):
        self._type = _type
        self._charset = charset

    @property
    def type(self):
        return self._type

    @property
    def charset(self):
        return self._charset
