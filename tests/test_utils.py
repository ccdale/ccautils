"""test file for utils.py file of ccautils module."""
import ccautils.utils as UT


def test_addToStringStr():
    """addToString test string input."""
    xstr = "A String"
    astr = " added"
    zstr = UT.addToString(xstr, astr)
    assert zstr == "A String added"


def test_addToStringList():
    """addToString test list input."""
    xstr = "A String"
    lstr = [" ", "added"]
    zstr = UT.addToString(xstr, lstr)
    assert zstr == "A String added"


def test_delimitStringList():
    """delimitString test list input."""
    delim = " "
    xadd = ["A", "String", "added"]
    zstr = UT.delimitString(xadd, delim)
    assert zstr == "A String added"


def test_makeDictFromString():
    """makeDictFromString test."""
    istr = "someparam   = somevalue,someotherparam =someothervalue  "
    xd = UT.makeDictFromString(istr)
    wd = {
        "someparam": "somevalue",
        "someotherparam": "someothervalue",
    }
    assert xd == wd


def test_padStr_left():
    """padStr on the left test."""
    xstr = "3"
    ystr = UT.padStr(xstr)
    assert ystr == " 3"


def test_padStr_right_zeros():
    """padStr on the right with zeros test."""
    xstr = "3"
    ystr = UT.padStr(xstr, 4, "0", False)
    assert ystr == "3000"


def test_reduceTime():
    """reduceTime test."""
    unit = 60
    secs = 100
    exp = (1, 40)
    got = UT.reduceTime(unit, secs)
    assert got == exp


def test_displayValue():
    """displayValue multi-values test."""
    val = 2
    label = "elephant"
    got = UT.displayValue(val, label)
    assert got == "2 elephants"


def test_displayValue_one():
    """displayValue single value test."""
    val = 1
    label = "elephant"
    got = UT.displayValue(val, label)
    assert got == "1 elephant"


def test_displayValue_zero():
    """displayValue zero value test."""
    val = 0
    label = "elephant"
    got = UT.displayValue(val, label)
    assert len(got) == 0


def test_secondsFromHMS():
    """secondsFromHMS test - no carry."""
    hms = "01:01:23.43"
    secs = UT.secondsFromHMS(hms)
    exp = 3600 + 60 + 23
    assert secs == exp


def test_secondsFromHMS_carry():
    """secondsFromHMS test with carry."""
    hms = "01:01:23.73"
    secs = UT.secondsFromHMS(hms)
    exp = 3600 + 60 + 23 + 1
    assert secs == exp


def test_hms_small_short():
    """hms test small short."""
    secs = 67
    got = UT.hms(secs)
    exp = "1 min and 7 secs"
    assert got == exp


def test_hms_small():
    """hms test small."""
    secs = 67
    got = UT.hms(secs, short=False)
    exp = "1 minute and 7 seconds"
    assert got == exp


def test_hms_long():
    """hms test long."""
    secs = 67
    got = UT.hms(secs, small=False, short=False)
    exp = "0 days, 0 hours, 1 minute and 7 seconds"
    assert got == exp


def test_hms_single():
    """hms test single."""
    secs = 86400 + 7200 + 300 + 34
    got = UT.hms(secs, single=True)
    exp = "1d 2h 5m 34s"
    assert got == exp


def test_hms_colons_full():
    """hms test colons full."""
    secs = 86400 + 7200 + 300 + 34
    got = UT.hms(secs, colons=True)
    exp = "01:02:05:34"
    assert got == exp


def test_hms_colons_short():
    """hms test short colons."""
    secs = 302
    got = UT.hms(secs, colons=True)
    exp = "05:02"
    assert got == exp


# def test_askMe():
#     """askMe string input test."""
#     query = "Please press the"
#     default = "enter key"
#     v = UT.askMe(query, default)
#     assert v == default
#
#
# def test_askMeNumeric():
#     """askMe numeric input test."""
#     query = "press 5 and enter"
#     default = "5"
#     v = UT.askMe(query, default)
#     assert v == "5"
