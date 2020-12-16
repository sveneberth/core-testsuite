import unittest


class TestUtils(unittest.TestCase):

	def test_escapeString(self):
		from viur.core.utils import escapeString

		self.assertEquals("None", escapeString(None))
		self.assertEquals("abcde", escapeString("abcdefghi", maxLength=5))
		self.assertEquals("&lt;html&gt;&&lt;/html&gt;", escapeString("<html>\n&\0</html>"))
