import pytest
import ccautils.utils as UT


def test_addToStringStr():
    xstr = "A String"
    astr = " added"
    zstr = UT.addToString(xstr, astr)
    assert zstr == "A String added"


def test_addToStringList():
    xstr = "A String"
    lstr = [" ", "added"]
    zstr = UT.addToString(xstr, lstr)
    assert zstr == "A String added"
