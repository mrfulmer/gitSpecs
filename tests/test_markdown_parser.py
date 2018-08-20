import unittest
from markdown_parser import md2html

class Test_md2html(unittest.TestCase):
    def test_html(self):
        self.assertAlmostEqual(md2html("test.md"), None)