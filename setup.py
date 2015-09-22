from __future__ import absolute_import

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.pytest_args))


setup(
    name="csvxls",
    description="Functions to read from CSV or XLS(X) files interchangeably",
    author="Yuki Izumi",
    author_email="yuki@kivikakk.ee",
    url="https://github.com/kivikakk/csvxls",
    long_description="""
Two functions to aid in reading CSV and XLS/XLSX files interchangeably,
while respecting Unicode.

read_csv_or_xls does its best to read its data argument (should be
bytes) as an Excel file.  If it fails, it tries to decode it as UTF-8.
If you hand it a (Unicode) string, it'll just return it.

utf8_reader gives you a CSV reader (like the csv library's) which
decodes its argument as UTF-8; the generator yields Unicode strings.
    """,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    license="kindest",
    version="0.2",
    packages=["csvxls"],
    install_requires=["six>=1,<2", "xlrd==0.9.3"],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
