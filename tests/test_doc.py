#!/usr/bin/env python3
import doctest
import zuikuihuoshou.core.i18n   # noqa: import it because it does change the locale
from zuikuihuoshou.test import setup_tests
import os
import unittest

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))


def importModule(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


class TestDoc(unittest.TestCase):
    verbose = False

    def check_doc(self, filename, subdir=None, name=None):
        if self.verbose:
            print("--- %s: Run tests" % filename)
        if not subdir:
            fullpath = os.path.join('..', 'doc', filename)
        else:
            fullpath = os.path.join(subdir, filename)
        failure, nb_test = doctest.testfile(
            fullpath, optionflags=doctest.ELLIPSIS, name=name)
        if failure:
            self.fail("error")
        if self.verbose:
            print("--- %s: End of tests" % filename)

    def check_module(self, name):
        if self.verbose:
            print("--- Test module %s" % name)
        module = importModule(name)
        failure, nb_test = doctest.testmod(module)
        if failure:
            self.fail("error")
        if self.verbose:
            print("--- End of test")

    def test_doc_directory(self):
        self.check_doc('developer.rst')
        self.check_doc('internals.rst')
        self.check_doc('regex.rst')

    def test_tests_directory(self):
        self.check_doc('regex_regression.rst', subdir='.')

    def test_zuikuihuoshou_core(self):
        self.check_module("zuikuihuoshou.core.bits")
        self.check_module("zuikuihuoshou.core.dict")
        self.check_module("zuikuihuoshou.core.i18n")
        self.check_module("zuikuihuoshou.core.text_handler")
        self.check_module("zuikuihuoshou.core.tools")

    def test_zuikuihuoshou_metadata(self):
        self.check_module("zuikuihuoshou.metadata.metadata")
        self.check_module("zuikuihuoshou.metadata.setter")

    def test_zuikuihuoshou_regex(self):
        self.check_module("zuikuihuoshou.regex.parser")
        self.check_module("zuikuihuoshou.regex.regex")
        self.check_module("zuikuihuoshou.regex.pattern")


if __name__ == "__main__":
    setup_tests()
    unittest.main()
