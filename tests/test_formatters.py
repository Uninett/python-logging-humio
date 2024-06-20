import logging
from unittest import TestCase

from humiologging.formatters import HumioJSONFormatter, HumioKVFormatter


class HumioKVFormatterTests(TestCase):

    def test_format(self):
        formatter = HumioKVFormatter()
        message = "This is the fisrt test's test"
        level = logging.ERROR
        record = logging.LogRecord(
            name='foo',
            level=logging.ERROR,
            pathname='/x/y/z.py',
            lineno=321,
            msg=message,
            args=(),
            exc_info=None
        )
        result = formatter.format(record)
        self.assertIn('name=foo', result)
        self.assertIn('asctime=', result)
        self.assertIn('args=None', result)
        self.assertIn(f'levelno={level}', result)
        self.assertIn('msg={}'.format(repr(message)), result)
        self.assertIn('formattedMessage={}'.format(repr(message)), result)


class HumioJSONFormatterTests(TestCase):

    def test_format(self):
        formatter = HumioJSONFormatter()
        record = logging.LogRecord(
            name='foo',
            level=logging.ERROR,
            pathname='/x/y/z.py',
            lineno=321,
            msg="This is a test",
            args=(),
            exc_info=None
        )
        result = formatter.format(record)
        result_attributes = result['events'][0]['attributes']
        self.assertEqual(result_attributes['msg'], "This is a test")
        self.assertEqual(result_attributes['levelno'], logging.ERROR)
