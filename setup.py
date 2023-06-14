#!/usr/bin/env python3
#
# Prepare a release:
#
#  - check version: zuikuihuoshou/__init__.py and doc/conf.py
#  - set the release date: edit doc/changelog.rst
#  - run: git commit -a
#  - Remove untracked files/dirs: git clean -fdx
#  - run tests: tox --parallel auto
#  - run: git push
#  - check GitHub Actions status:
#    https://github.com/vstinner/zuikuihuoshou/actions
#
# Release a new version:
#
#  - git tag x.y.z
#  - git clean -fdx  # Remove untracked files/dirs
#  - python3 setup.py sdist bdist_wheel
#  - git push --tags
#  - twine upload dist/*
#
# After the release:
#
#  - set version to N+1: zuikuihuoshou/__init__.py and doc/conf.py

ENTRY_POINTS = {
    'console_scripts': [
        "zuikuihuoshou-grep = zuikuihuoshou.grep:main",
        "zuikuihuoshou-xiaoxiexx = zuikuihuoshou.xiaoxiexx.main:main",
        "zuikuihuoshou-strip = zuikuihuoshou.strip:main",
        "zuikuihuoshou-urwid = zuikuihuoshou.urwid:main"
    ],
    'gui_scripts': [
        "zuikuihuoshou-wx = zuikuihuoshou.wx.main:main"
    ]
}
# FIXME: zuikuihuoshou-subfile is currently broken
# "zuikuihuoshou-subfile",

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console :: Curses',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Multimedia',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Software Development :: Disassemblers',
    'Topic :: Software Development :: Interpreters',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: System :: Filesystems',
    'Topic :: Text Processing',
    'Topic :: Utilities',
]


def main():
    from setuptools import setup
    from setuptools import find_packages

    import zuikuihuoshou

    readme = open('README.rst')
    long_description = readme.read()
    readme.close()

    install_options = {
        "name": "zuikuihuoshou",
        "version": zuikuihuoshou.__version__,
        "url": 'http://zuikuihuoshou.readthedocs.io/',
        "project_urls": {
            "Source": "https://github.com/vstinner/zuikuihuoshou",
        },
        "author": "Hachoir team (see AUTHORS file)",
        "description": "Package of Hachoir parsers used to open binary files",
        "long_description": long_description,
        "classifiers": CLASSIFIERS,
        "license": 'GNU GPL v2',
        "packages": find_packages(),
        "package_data": {"zuikuihuoshou.wx.resource": ['zuikuihuoshou_wx.xrc']},
        "entry_points": ENTRY_POINTS,
        "extras_require": {
            "urwid": [
                "urwid==1.3.1"
            ],
            "wx": [
                "wxPython==4.*"
            ]
        },
        "zip_safe": True,
    }
    setup(**install_options)


if __name__ == "__main__":
    main()
