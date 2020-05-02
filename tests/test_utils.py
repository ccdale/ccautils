"""Test file for utils.py file of ccautils module."""
import datetime
import io
import sys
import time

import pytest

import ccautils.utils as UT


def test_addToStringStr():
    """Input strings are concatenated."""
    xstr = "A String"
    astr = " added"
    zstr = UT.addToString(xstr, astr)
    assert zstr == "A String added"


def test_addToString_not_str_input():
    """Input strings are concatenated."""
    xstr = []
    astr = " added"
    zstr = UT.addToString(xstr, astr)
    assert zstr == astr


def test_addToString_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        UT.addToString("", int(23))


def test_addToStringList():
    """List is exploded and each member is concatenated."""
    xstr = "A String"
    lstr = [" ", "added"]
    zstr = UT.addToString(xstr, lstr)
    assert zstr == "A String added"


def test_addToString_mixed_List():
    """List is exploded and each member is concatenated."""
    xstr = "A String"
    lstr = [" ", 22, "added"]
    zstr = UT.addToString(xstr, lstr)
    assert zstr == "A String added"


def test_delimitString_string():
    """It splits the input string and concatenates each string with the delimeter."""
    delim = " | "
    xadd = "A String Added"
    zstr = UT.delimitString(xadd, delim)
    assert zstr == "A | String | Added"


def test_delimitStringList():
    """It concatenates each string with the delimeter."""
    delim = " "
    xadd = ["A", "String", "added"]
    zstr = UT.delimitString(xadd, delim)
    assert zstr == "A String added"


def test_delimitString_exception():
    """It raises a ValueError Exception."""
    with pytest.raises(ValueError):
        UT.delimitString(int(32))


def test_makeDictFromString():
    """It removes extraneous white space and forms a dict from the string."""
    istr = "someparam   = somevalue,someotherparam =someothervalue  "
    xd = UT.makeDictFromString(istr)
    wd = {
        "someparam": "somevalue",
        "someotherparam": "someothervalue",
    }
    assert xd == wd


def test_makeDictFromString_not_matching():
    """It returns an empty dict."""
    istr = "someparam    somevalue,someotherparam someothervalue  "
    xd = UT.makeDictFromString(istr)
    assert xd == {}


def test_makeDictFromString_exception():
    """It raises a ValueError Exception."""
    with pytest.raises(TypeError):
        UT.makeDictFromString(int(32))


def test_padStr_left():
    """It pads on the left."""
    xstr = "3"
    ystr = UT.padStr(xstr)
    assert ystr == " 3"


def test_padStr_right_zeros():
    """It pads on the right with zeros."""
    xstr = "3"
    ystr = UT.padStr(xstr, 4, "0", False)
    assert ystr == "3000"


def test_padStr_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        UT.padStr(int(32))


def test_reduceTime():
    """It returns a tuple of unit and modulo remainder."""
    unit = 60
    secs = 100
    exp = (1, 40)
    got = UT.reduceTime(unit, secs)
    assert got == exp


def test_reduceTime_exception():
    """It raises a ValueError Exception."""
    with pytest.raises(ValueError):
        UT.reduceTime(0, 22)


def test_displayValue():
    """It pluralises the input label."""
    val = 2
    label = "elephant"
    got = UT.displayValue(val, label)
    assert got == "2 elephants"


def test_displayValue_one():
    """It doesn't pluralise the input label."""
    val = 1
    label = "elephant"
    got = UT.displayValue(val, label)
    assert got == "1 elephant"


def test_displayValue_zero():
    """It pluralises the input label."""
    val = 0
    label = "elephant"
    got = UT.displayValue(val, label)
    assert len(got) == 0


def test_displayValue_exception():
    """It raises a ValueError Exception."""
    with pytest.raises(TypeError):
        UT.displayValue([], "elephant")


def test_secondsFromHMS():
    """It doesn't carry the under 500 milliseconds into seconds."""
    hms = "01:01:23.43"
    secs = UT.secondsFromHMS(hms)
    exp = 3600 + 60 + 23
    assert secs == exp


def test_secondsFromHMS_carry():
    """It carries the over 500 milliseconds into seconds."""
    hms = "01:01:23.73"
    secs = UT.secondsFromHMS(hms)
    exp = 3600 + 60 + 23 + 1
    assert secs == exp


def test_secondsFromHMS_one_short():
    """It doesn't carry the under 500 milliseconds into seconds."""
    hms = "01:23.43"
    secs = UT.secondsFromHMS(hms)
    exp = 60 + 23
    assert secs == exp


def test_secondsFromHMS_two_short():
    """It doesn't carry the under 500 milliseconds into seconds."""
    hms = "23.43"
    secs = UT.secondsFromHMS(hms)
    exp = 23
    assert secs == exp


def test_secondsFromHMS_exception():
    """It raises a ValueError Exception."""
    with pytest.raises(AttributeError):
        UT.secondsFromHMS([])


def test_hms_small_short():
    """It returns a short time string with short labels."""
    secs = 67
    got = UT.hms(secs)
    exp = "1 min and 7 secs"
    assert got == exp


def test_hms_small():
    """It returns a short time string."""
    secs = 67
    got = UT.hms(secs, short=False)
    exp = "1 minute and 7 seconds"
    assert got == exp


def test_hms_long():
    """It returns a full time string, with zero values."""
    secs = 67
    got = UT.hms(secs, small=False, short=False)
    exp = "0 days, 0 hours, 1 minute and 7 seconds"
    assert got == exp


def test_hms_single():
    """It returns single letter labels."""
    secs = 86400 + 7200 + 300 + 34
    got = UT.hms(secs, single=True)
    exp = "1d 2h 5m 34s"
    assert got == exp


def test_hms_colons_full():
    """It returns days, hours, minutes and seconds, padded with zeros, delimited by colons."""
    secs = 86400 + 7200 + 300 + 34
    got = UT.hms(secs, colons=True)
    exp = "01:02:05:34"
    assert got == exp


def test_hms_colons_short():
    """It returns only minutes and seconds, padded with zeros, delimited by colons."""
    secs = 302
    got = UT.hms(secs, colons=True)
    exp = "05:02"
    assert got == exp


def test_hms_exception():
    """It raises a ValueError Exception."""
    with pytest.raises(TypeError):
        UT.hms([])


def test_decomplexifyhms():
    """It returns a list containing 1 string."""
    got = UT.decomplexifyhms([0], 0, [["day"]], 0, 0)
    exp = ["0 days"]
    assert got == exp


def test_decomplexifyhms_exception():
    """It raises a ValueError Exception."""
    with pytest.raises(IndexError):
        UT.decomplexifyhms([1], 2, [], 1, 1)


def test_askMe_exception():
    """It raises a ValueError Exception."""
    with pytest.raises(TypeError):
        UT.askMe([], "splodge")


def test_askMe_stdin_redirect():
    """String input test."""
    original_stdin = sys.stdin
    sys.stdin = io.StringIO("hello\n")
    query = "Please press the"
    default = "enter key"
    v = UT.askMe(query, default)
    sys.stdin = original_stdin
    assert v == "hello"


def test_askMe_stdin_redirect_default():
    """String input test."""
    original_stdin = sys.stdin
    sys.stdin = io.StringIO("\n")
    query = "Please press the"
    default = "enter key"
    v = UT.askMe(query, default)
    sys.stdin = original_stdin
    assert v == default


def test_tsFromDt():
    """It returns an INT."""
    dt = datetime.datetime(year=2020, month=3, day=6, hour=16, minute=19, second=12)
    exp = 1583511552
    got = UT.tsFromDt(dt)
    assert got == exp


def test_fuzzyExpires_Expired():
    """It returns the string 'EXPIRED'."""
    dt = datetime.datetime(year=2020, month=3, day=6, hour=16, minute=19, second=12)
    expts = 1583511552
    expstr = "EXPIRED"
    gotts, gotstr = UT.fuzzyExpires(dt)
    assert expstr == gotstr and expts == gotts


def test_fuzzyExpires_gt_year():
    """It returns 1 year and 2 months."""
    ts = int(time.time())
    ts += (86400 * 365) + (86400 * 70)
    expstr = "1 year 2 months"
    dt = datetime.datetime.fromtimestamp(ts)
    gotts, gotstr = UT.fuzzyExpires(dt)
    assert gotstr == expstr


def test_fuzzyExpires_gt_month():
    """It returns 1 month and some days."""
    ts = int(time.time())
    ts += 86400 * 33
    dt = datetime.datetime.fromtimestamp(ts)
    gotts, gotstr = UT.fuzzyExpires(dt)
    assert gotstr.startswith("1 month")


def test_fuzzyExpires_lt_month():
    """It returns 23 days and some hours."""
    ts = int(time.time())
    ts += 86400 * 23
    dt = datetime.datetime.fromtimestamp(ts)
    gotts, gotstr = UT.fuzzyExpires(dt)
    assert gotstr.startswith("23 days")


def test_fuzzyExpires_lt_day():
    """It returns 2 hours 20 minutes and some seconds."""
    ts = int(time.time())
    ts += (3600 * 2) + (60 * 20)
    dt = datetime.datetime.fromtimestamp(ts)
    gotts, gotstr = UT.fuzzyExpires(dt)
    assert gotstr.startswith("2 hours 20 minutes")


def test_runCmd():
    """It can run the unix ls command without error"""
    cmd = ["ls"]
    res, stdout, stderr = UT.runCmd(cmd)
    assert 0 == res
