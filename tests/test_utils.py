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


def test_delimitStringList():
    xstr = "A"
    delim = " "
    xadd = ["String", "added"]
    zstr = UT.delimitString(xstr, xadd, delim)
    assert zstr == "A String added"


def test_makeDictFromString():
    istr = "someparam   = somevalue,someotherparam =someothervalue  "
    xd = UT.makeDictFromString(istr)
    wd = {
        "someparam": "somevalue",
        "someotherparam": "someothervalue",
    }
    assert xd == wd


def test_askMe():
    query = "Please press the"
    default = "enter key"
    v = UT.askMe(query, default)
    assert v == default


def test_askMeNumeric():
    query = "press 5 and enter"
    default = "5"
    v = UT.askMe(query, default)
    assert v == "5"
