#!/usr/bin/env python
# coding=utf-8
from textwrap import dedent

import yaml as pyyaml
from pytest import mark

import pureyaml
from pureyaml.encoder import node_encoder
from pureyaml.nodes import *  # noqa
from tests.utils import MultiTestCaseBase


class EncodeTestCase(MultiTestCaseBase):
    it_handles_dict__data = {'name': 'John Smith', 'age': 33}
    it_handles_dict__test_pureyaml_dump__not_PYPY = dedent("""
        age: 33
        name: John Smith
    """)[1:]
    it_handles_dict__test_pureyaml_dump__PYPY = dedent("""
        name: John Smith
        age: 33
    """)[1:]
    it_handles_dict__test_pyyaml_dump = dedent("""
        age: 33
        name: John Smith
    """)[1:]
    it_handles_dict__test_encode = Map(  # :off
        (Str('name'), Str('John Smith')),
        (Str('age'), Int(33)),
    )  # :on


def pureyaml_dump(data):
    text = pureyaml.dump(data)
    # print('\n' + text)
    return text


def pyyaml_dump(data):
    text = pyyaml.dump(data, default_flow_style=False)
    # print('\n' + text)
    return text


def encode(data):
    nodes = node_encoder(data)
    return nodes


def sanity(data):
    text = pureyaml.dump(data)
    _data = pureyaml.load(text)
    return _data


@mark.parametrize('case', EncodeTestCase.keys('encode'))
def test_encode(case):
    data, expected = EncodeTestCase.get('encode', case)
    assert encode(data) == expected


@mark.parametrize('case', EncodeTestCase.keys('pureyaml_dump'))
def test_pureyaml_dump(case):
    data, expected = EncodeTestCase.get('pureyaml_dump', case)
    assert pureyaml_dump(data) == expected


@mark.parametrize('case', EncodeTestCase.keys('pureyaml_dump'))
def test_pureyaml_sanity(case):
    data, _ = EncodeTestCase.get('pureyaml_dump', case)
    assert sanity(data) == data


@mark.parametrize('case', EncodeTestCase.keys('pyyaml_dump'))
def test_pyyaml_dump(case):
    data, expected = EncodeTestCase.get('pyyaml_dump', case)
    assert pyyaml_dump(data) == expected