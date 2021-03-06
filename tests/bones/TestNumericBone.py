import unittest


class TestNumericBone(unittest.TestCase):

	def test_isEmpty_default_bone(self):
		from viur.core.bones import numericBone
		self._run_tests(numericBone())

	def test_isEmpty_emptyNone(self):
		from viur.core.bones import numericBone
		self._run_tests(numericBone(getEmtpyValueFunc=lambda: None))

	def test_isEmpty_precision(self):
		from viur.core.bones import numericBone
		self._run_tests(numericBone(precision=2))

	def test_isEmpty_precision_emptyNone(self):
		from viur.core.bones import numericBone
		self._run_tests(numericBone(precision=2, getEmtpyValueFunc=lambda: None))

	def _run_tests(self, bone):
		self.assertFalse(bone.isEmpty(123))
		self.assertFalse(bone.isEmpty("123"))
		self.assertFalse(bone.isEmpty("123.456"))
		self.assertFalse(bone.isEmpty("123,456"))
		self.assertFalse(bone.isEmpty(123.456))

		self.assertTrue(bone.isEmpty(""))
		self.assertTrue(bone.isEmpty(None))
		self.assertTrue(bone.isEmpty([]))
		self.assertTrue(bone.isEmpty(bone.getEmptyValue()))
		self.assertTrue(bone.isEmpty(str(bone.getEmptyValue())))
		if bone.getEmptyValue() is not None:
			self.assertTrue(bone.isEmpty(float(bone.getEmptyValue())))
			self.assertTrue(bone.isEmpty(int(bone.getEmptyValue())))
