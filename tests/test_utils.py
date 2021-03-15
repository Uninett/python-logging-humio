import logging
import sys
from unittest import TestCase

from humiologging.utils import make_safe_for_json


class MakeSafeForJSONTests(TestCase):

    def test_primitive_types_should_not_be_changed(self):
        recorddict = {
            'int': 5,
            'none': None,
        }
        result = make_safe_for_json(recorddict)
        self.assertEqual(result, recorddict)

    def test_complesx_types_should_be_changed(self):
        class SomeClass:
            pass

        recorddict = {
            'someobj': SomeClass(),
        }
        result = make_safe_for_json(recorddict)
        self.assertEqual(result['someobj'], repr(SomeClass()))
