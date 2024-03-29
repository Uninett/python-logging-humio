================
Logging to Humio
================

.. image:: https://github.com/Uninett/python-logging-humio/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/Uninett/python-logging-humio/actions/workflows/ci.yml
    :alt: CI Status

.. image:: https://img.shields.io/pypi/v/humiologging
    :target: https://pypi.org/project/humiologging/
    :alt: PyPI: humiologging

.. image:: https://img.shields.io/pypi/pyversions/humiologging
    :alt: Python versions: 3.7, 3.8, 3.9, 3.10, 3.11

.. image:: https://img.shields.io/pypi/l/humiologging
    :alt: License: Apache 2.0

This package contains logging handlers and formatters useful for logging
to `Humio <https://www.humio.com/>`_. It's sole runtime dependency is
`humiolib <https://github.com/humio/python-humio>`_.

Runs and tested on Python 3.7, 3.8, 3.9, 3.10, 3.11.

Contents
========

Installation
------------

The pacakage on PyPI is named ``humiologging``, same as the package name.
Install with for instance ``pip install humiologging``.

Formatters
----------

``humiologging.formatters.HumioKVFormatter``
    Turns every attribute on the log record into a key-value pair, as suitable
    for the Humio "kv"-parser. Use with ``HumioHandler``.

``humiologging.formatters.HumioJSONFormatter``
    Turns the log-record into a json object, as suitable for the Humio
    "json"-parser. Used by ``HumioJSONHandler``.

Handlers
--------

``humiologging.handlers.HumioHandler``
    Sends line-based text log messages to Humio. You need to use a formatter
    that Humio can parse, like ``HumioKVFormatter``.

``humiologging.handlers.HumioJSONHandler``
    Sends json-formatted log messages to Humio. Does not need a formatter.

Positional arguments:

    :humio_host: The url of the humio ingest host
    :ingest_token: The API token for a Humio repo

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

With no parser set
------------------

    import logging
    logging.basicConfig(handlers=[HumioJSONHandler(host, token)])
    logging.error('This is a test')

In Humio you should get a single entry with one key for every attribute in the
log record. One additional key `formattedMessage` contains the human-readable
format set in the logging config as a string.

For parser ``kv``
-----------------

    import logging
    logging.basicConfig(handlers=[HumioHandler(host, token).setFormatter(HumioKVFormatter())])
    logging.error('This is a test')

In Humio you should get a single record with a string containing many key=value
pairs. One additional key `formattedMessage` contains the human-readable
format set in the logging config as a string.
