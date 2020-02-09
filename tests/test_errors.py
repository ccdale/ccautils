"""Test file for errors.py file of ccautils module."""
import pytest

import ccautils.errors as ET
from ccautils.errors import errorExit
from ccautils.errors import errorNotify
from ccautils.errors import errorRaise


class TheException(Exception):
    pass


def test_formatter():
    """Arguments are concatenated."""
    fname = "test_formatter"
    msg = "This is the test exception."
    e = TheException(msg)
    expect = f"Error in {fname}: TheException: {msg}\n"
    got = ET.formatErrorMsg(fname, e)
    assert got == expect


def test_raises():
    """It raises TheException Exception."""
    fname = "test_raises"
    msg = "This is the test exception."
    with pytest.raises(TheException):
        errorRaise(fname, TheException(msg))


def test_notify(capsys):
    """It writes the error to stderr."""
    fname = "test_notify"
    msg = "This is the test exception"
    e = TheException(msg)
    errorNotify(fname, e)
    captured = capsys.readouterr()
    assert captured.err == f"Error in {fname}: TheException: {msg}\n"


def test_raises():
    """It attempts sys.exit."""
    fname = "test_notify"
    msg = "This is the test exception"
    e = TheException(msg)
    with pytest.raises(SystemExit):
        errorExit(fname, e, 1)
