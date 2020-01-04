import unittest
from statipie.mime import create_from_extension
from statipie.mime import UTF_8
from statipie.mime import (TEXT_HTML, TEXT_CSS, APPLICATION_JAVASCRIPT,
                           IMAGE_BMP, IMAGE_PNG,)


class MimeTest(unittest.TestCase):
    def test_create_from_extension(self):
        cases = (
            ('.html', TEXT_HTML, UTF_8),
            ('.css', TEXT_CSS, UTF_8),

            ('.js', APPLICATION_JAVASCRIPT, UTF_8),

            ('.bmp', IMAGE_BMP, None),
            ('.png', IMAGE_PNG, None),
        )
        for ext, expected_type, expected_charset in cases:
            with self.subTest(ext=ext):
                mime = create_from_extension(ext)

                self.assertEqual(expected_type, mime.type)
                self.assertEqual(expected_charset, mime.charset)
