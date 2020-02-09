"""Test file for utils.py file of ccautils module."""
import pytest

import ccautils.utils as UT


def test_addToStringStr():
    """Input strings are concatenated."""
    xstr = "A String"
    astr = " added"
    zstr = UT.addToString(xstr, astr)
    assert zstr == "A String added"


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
    with pytest.raises(TypeError):
        UT.decomplexifyhms()


@pytest.mark.ask
def test_askMe():
    """String input test."""
    query = "Please press the"
    default = "enter key"
    v = UT.askMe(query, default)
    assert v == default


@pytest.mark.ask
def test_askMeNumeric():
    """Numeric input test."""
    query = "press 5 and enter"
    default = "5"
    v = UT.askMe(query, default)
    assert v == "5"
