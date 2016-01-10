#!/usr/bin/env python
# coding=utf-8
"""
==============
pureyaml
==============

Yet another yaml parser, in pure python.

"""
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()

import logging

from pureyaml.encoder import YAMLEncoder
from ._compat import NullHandler
from .decoder import YAMLDecoder

logging.getLogger(__name__).addHandler(NullHandler())

__author__ = 'Manu Phatak'
__email__ = 'bionikspoon@gmail.com'
__version__ = '0.1.0'


def dump(obj, fp=None, cls=None, indent=None, sort_keys=False, **kw):
    cls = cls or YAMLEncoder
    if fp:
        iterable = cls(indent=indent, sort_keys=sort_keys, **kw).iterencode(obj)
        for chunk in iterable:
            fp.write(chunk)
    else:
        return dumps(obj, cls=cls, indent=indent, sort_keys=sort_keys, **kw)


def dumps(obj, cls=None, indent=None, default=None, sort_keys=False, **kw):
    cls = cls or YAMLEncoder
    return cls(indent=indent, default=default, sort_keys=sort_keys, **kw).encode(obj)


def load(s, **kwargs):
    return loads(s, **kwargs)


def loads(s, cls=None, **kwargs):
    if not isinstance(s, str):
        raise TypeError('the YAML object must be str, not {!r}'.format(s.__class__.__name__))

    cls = cls or YAMLDecoder
    return cls(**kwargs).decode(s)
