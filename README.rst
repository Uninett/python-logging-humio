================
Logging to Humio
================

This package contains logging handlers and formatters useful for logging
to `Humio <https://www.humio.com/>`_. It's sole runtime dependency is
`humiolib <https://github.com/humio/python-humio>`_.

Contents
========

Formatters
----------

``humiologging.formatters.HumioKVFormatter``
    Turns every attribute on the log record into a key-value pair, as suitable
    for the Humio "kv"-parser. Use with ``HumioHandler``.

Handlers
--------

``humiologging.handlers.HumioHandler``
    Sends line-based text log messages to Humio. You need to use a formatter
    that Humio can parse, like ``HumioKVFormatter``.

``humiologging.handlers.HumioJSONHandler``
    Sends json-formatted log messages to Humio. Does not need a formatter. If
    a formatter is set, this will affect the key ``formattedRecord``.

Positional arguments:

    humio_host, ingest_token

Keyword arguments:

    :level: A log-level
    :tags: A dictionary of key value items that will be addded to each record
    :add_host_tag:
        Whether to automatically add the hostname/ip-address where
        the loghandler is used as a tag

Be careful with setting many tags, see
`Humio Documentation: Tagging <https://docs.humio.com/docs/parsers/tagging/>`_

Testing
=======

Run automated tests with `tox <https://tox.readthedocs.io/en/latest/>`_.

To test against humio: you need the hostname of the humio instance and an
ingest_token for a repo with parser set to the handler you want to test.

For parser ``json``::

    import logging
    logging.basicConfig(handlers=[HumioJSONHandler(host, token)])
    logging.error('This is a test')

In humio you should get a single record with two keys: one ``record`` key that
dumps everything in the log-record, and one ``formattedRecord`` key that has
the value ``"This is a test"``.

For parser ``kv``::

    import logging
    logging.basicConfig(handlers=[HumioHandler(host, token).setFormatter(HumioKVFormatter())])
    logging.error('This is a test')

In humio you should get a single record with two keys: one ``record`` key that
dumps everything in the log-record, and one ``formattedRecord`` key that has
the value ``"This is a test"``.
