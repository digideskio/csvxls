# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import os

from csvxls import read_csv_or_xls
from csvxls import utf8_reader


def test_read_csv_or_xls_csv():
    with open(os.path.join(os.path.dirname(__file__), 'utf8.csv'), 'rb') as f:
        data = f.read().decode('utf8')

    assert read_csv_or_xls(data) == '泉,雪\n泉,海里\n'
    assert read_csv_or_xls(data.encode('utf8')) == '泉,雪\n泉,海里\n'

    for filename in ('test.xls', 'test.xlsx'):
        with open(os.path.join(os.path.dirname(__file__), filename), 'rb') as f:
            data = f.read()

        assert read_csv_or_xls(data) == '泉,雪\r\n泉,海里\r\n'


def test_utf8_reader():
    with open(os.path.join(os.path.dirname(__file__), 'utf8.csv'), 'rb') as f:
        data = f.read().decode('utf8')

    rows = list(utf8_reader(data))

    assert len(rows) == 2
    assert rows[0] == ['泉', '雪']
    assert rows[1] == ['泉', '海里']
