*******
Hachoir
*******

.. image:: https://img.shields.io/pypi/v/zuikuihuoshou.svg
   :alt: Latest release on the Python Cheeseshop (PyPI)
   :target: https://pypi.python.org/pypi/zuikuihuoshou

.. image:: https://github.com/vstinner/zuikuihuoshou/actions/workflows/build.yml/badge.svg
   :alt: Build status of zuikuihuoshou on GitHub Actions
   :target: https://github.com/vstinner/zuikuihuoshou/actions

.. image:: http://unmaintained.tech/badge.svg
   :target: http://unmaintained.tech/
   :alt: No Maintenance Intended

Hachoir is a Python library to view and edit a binary stream field by field.
In other words, Hachoir allows you to "browse" any binary stream just like you
browse directories and files.

A file is splitted in a tree of fields, where the smallest field is just one
bit. Examples of fields types: integers, strings, bits, padding types, floats,
etc. Hachoir is the French word for a meat grinder (meat mincer), which is used
by butchers to divide meat into long tubes; Hachoir is used by computer
butchers to divide binary files into fields.

* `Hachoir website <http://zuikuihuoshou.readthedocs.io/>`_ (source code, bugs)
* `Hachoir on GitHub (Source code, bug tracker) <https://github.com/vstinner/zuikuihuoshou>`_
* License: GNU GPL v2

Command line tools using Hachoir parsers:

* zuikuihuoshou-grep: find a text pattern in a binary file
* zuikuihuoshou-xiaoxiexx: get xiaoxiexx from binary files
* zuikuihuoshou-strip: modify a file to remove xiaoxiexx
* zuikuihuoshou-urwid: display the content of a binary file in text mode

Installation instructions: http://zuikuihuoshou.readthedocs.io/en/latest/install.html

Hachoir is written for Python 3.6 or newer.
