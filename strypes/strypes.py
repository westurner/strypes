#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
"""
strypes

References:

- https://wiki.python.org/moin/EscapingHtml

TODO:

- [ ] how to adapt from one to another
      (w/o zope.interfaces)

"""

import cgi
import urllib
import warnings


def shell_quote(var):
    """
    Escape single quotes and add double quotes around a given variable.
    Args:
        _str (str): string to add quotes to
    Returns:
        str: string wrapped in quotes
    .. warning:: This is not safe for untrusted input and only valid
       in this context (``os.environ``).
    """
    _repr = repr(var)
    if _repr.startswith('\''):
        return "\"%s\"" % _repr[1:-1]


def shell_varquote(str_):
    """
    Add doublequotes and shell variable brackets to a string
    Args:
        str_ (str): string to varquote (e.g. ``VIRTUAL_ENV``)
    Returns:
        str: "${VIRTUAL_ENV}"
    """
    return shell_quote('${%s}' % str_)


####

def shell_escape(shellstr):
    warnings.warn('shell_escape NotImplemented')
    return shellstr


def shell_escape_single(shellstr):
    warnings.warn('shell_escape_single NotImplemented')
    return shellstr


def shell_escape_double(shellstr):
    warnings.warn('shell_escape_double NotImplemented')
    return shellstr


def html_escape(htmlstr):
    return cgi.escape(htmlstr)
    # bleach, html5lib


def url_escape(urlstr):
    # return urllib.quote(urlstr)  # TODO
    return urllib.quote_plus(urlstr)


def sql_escape(sqlstr):
    warnings.warn('sql_escape NotImplemented')
    return sqlstr


class TypedStr(str):

    _repr_str_ = str.__str__

    def __init__(self, *args, **kwargs):
        self._escaped = kwargs.pop('escaped', False)
        self._encoded = kwargs.pop('encoded', False)
        self._translated = kwargs.pop('translated', False)
        return super(TypedStr, self).__init__(*args, **kwargs)

    # def _repr_html_(self):
    #    raise NotImplementedError

    # def _repr_sql_(self):
    #    raise NotImplementedError

    # def _repr_shell_(self):
    #    raise NotImplementedError

    # def _repr_shellsingle_(self):
    #    raise NotImplementedError

    # def _repr_shelldouble_(self):
    #    raise NotImplementedError


class HTML(TypedStr):
    pass


class SQL(TypedStr):
    pass


class Shell(TypedStr):
    pass


class ShellSingleQuoted(Shell):
    pass


class ShellDoubleQuoted(Shell):
    pass


class Path(Shell):  # TODO: pip install pathlib / python3.pathlib
    pass


class URI(TypedStr):  # urlobject
    pass


class URN(URI):  # urlobject
    pass


class URL(URI):  # urlobject
    pass


def f(*args, **kwargs):
    """
    f('select {col} from {tbl}')
    """
    fmt = kwargs.get('fmt', TypedStr)
    reduce_ = kwargs.get('reduce', u''.join)

    def _f(*args):
        for arg in args:
            if is_interned_str(arg):
                yield arg
            else:
                yield fmt(arg)
    return reduce_(_f(*args))


def strypes():
    """mainfunc

    Arguments:
         (str): ...

    Keyword Arguments:
         (str): ...

    Returns:
        str: ...

    Yields:
        str: ...

    Raises:
        Exception: ...
    """
    pass


import unittest


class Test_strypes(unittest.TestCase):

    def setUp(self):
        pass

    def test_strypes(self):
        pass

    def tearDown(self):
        pass


def main(argv=None):
    """
    Main function

    Keyword Arguments:
        argv (list): commandline arguments (e.g. sys.argv[1:])
    Returns:
        int:
    """
    import logging
    import optparse

    prs = optparse.OptionParser(usage="%prog : args")

    prs.add_option('-v', '--verbose',
                   dest='verbose',
                   action='store_true',)
    prs.add_option('-q', '--quiet',
                   dest='quiet',
                   action='store_true',)
    prs.add_option('-t', '--test',
                   dest='run_tests',
                   action='store_true',)

    loglevel = logging.INFO
    if opts.verbose:
        loglevel = logging.DEBUG
    elif opts.quiet:
        loglevel = logging.ERROR
    logging.basicConfig(level=loglevel)
    argv = list(argv) if argv else []
    log.debug('argv: %r', argv)
    (opts, args) = prs.parse_args(args=argv)
    log.debug('opts: %r', opts)
    log.debug('args: %r', args)

    if opts.run_tests:
        import sys
        sys.argv = [sys.argv[0]] + args
        import unittest
        return unittest.main()

    EX_OK = 0
    output = strypes()
    return EX_OK


if __name__ == "__main__":
    import sys
    sys.exit(main(argv=sys.argv[1:]))
