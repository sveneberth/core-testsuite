#!/usr/bin/python

import unittest

from tests import bones, utils
from tests.utils import TestUtils


def monkeyPatch():
	"""Monkey patch libs to work without google cloud environment"""
	import sys
	import mock

	MOCK_MODULES = ['webob',
					'google.cloud.logging',
					'google.cloud.logging.resource',
					'google',
					'google.cloud',
					'google.protobuf',
					'google.auth',
					'google.auth.default',
					'google.cloud.datastore',
					'google.cloud.exceptions']

	for mod_name in MOCK_MODULES:
		sys.modules[mod_name] = mock.Mock()

	import google
	google.auth.default = mock.Mock(return_value=(mock.Mock(), mock.Mock()))

	import logging
	class NoopHandler(logging.Handler):
		def __init__(self, *args, **kwargs):
			super().__init__(level=kwargs.get("level", logging.NOTSET))

		transport = mock.Mock()
		resource = mock.Mock()
		labels = mock.Mock()

	sys.modules['google.cloud.logging.handlers'] = tmp = mock.Mock()
	tmp.CloudLoggingHandler = NoopHandler

	sys.modules['google.cloud.logging.handlers.handlers'] = tmp = mock.Mock()
	tmp.EXCLUDED_LOGGER_DEFAULTS = []


if __name__ == '__main__':
	monkeyPatch()

	# initialize the test suite
	loader = unittest.TestLoader()
	suite = unittest.TestSuite()

	# add tests to the test suite
	suite.addTests(loader.loadTestsFromModule(bones))
	suite.addTests(loader.loadTestsFromTestCase(TestUtils))

	# initialize a runner, pass it your suite and run it
	runner = unittest.TextTestRunner(verbosity=3)
	result = runner.run(suite)
