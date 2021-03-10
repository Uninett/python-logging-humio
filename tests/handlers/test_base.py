from unittest import TestCase

from humiologging.handlers.base import BaseHumioHandler


class BaseHumioHandlerTests(TestCase):

    def test_init_only_postional_args(self):
        handler = BaseHumioHandler('foo', 'bar')
        self.assertEqual(handler.humio_host, 'foo')
        self.assertEqual(handler.ingest_token, 'bar')
        self.assertTrue(handler.tags is None)

    def test_init_has_tags(self):
        tags = {'foo': 'bar'}
        handler = BaseHumioHandler('foo', 'bar', tags=tags)
        self.assertTrue(isinstance(handler.tags, dict))
        self.assertEqual(handler.tags['foo'], 'bar')

    def test_init_add_host_tag_is_true(self):
        handler = BaseHumioHandler('foo', 'bar', add_host_tag=True)
        self.assertTrue(isinstance(handler.tags, dict))
        self.assertIn('host', handler.tags)

    def test_emit(self):
        handler = BaseHumioHandler('foo', 'bar')
        with self.assertRaises(NotImplementedError):
            handler.emit(None)
