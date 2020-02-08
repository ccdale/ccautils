"""test file for fileutils.py file of ccautils module."""
import os

import ccautils.fileutils as FT


testfile = os.environ.get("HOME") + "/testfile-deleteme"
renamefile = os.path.dirname(testfile) + "/renamed-testfile-deleteme"
testlines = ["one\n", "two\n", "Three"]


def test_fileExists():
    """fileExists file exists test."""
    got = FT.fileExists(__file__)
    assert got is True


def test_fileExists_nonexist():
    """fileExists file doesn't exist test."""
    got = FT.fileExists("/non-existant")
    assert got is False


def test_dirExists():
    """dirExists directory exists test."""
    dird = os.path.dirname(__file__)
    got = FT.dirExists(dird)
    assert got is True


def test_dfExists():
    """dfExists directory exists test."""
    dird = os.path.dirname(__file__)
    got = FT.dfExists(dird)
    assert got is True


def test_absPath():
    """absPath file transform test."""
    tpath = "~/.bashrc"
    epath = os.environ.get("HOME") + "/.bashrc"
    got = FT.absPath(tpath)
    assert got == epath


def test_fileTouch():
    """fileTouch test."""
    FT.fileTouch(testfile)
    assert FT.fileExists(testfile) is True


def test_rename():
    """rename file test."""
    FT.rename(testfile, renamefile)
    assert FT.fileExists(renamefile) is True


def test_fileDelete():
    """fileDelete test."""
    FT.fileDelete(renamefile)
    assert FT.fileExists(renamefile) is False


def test_fileSize():
    """fileSize test."""
    with open(testfile, "w") as ofn:
        ofn.writelines(testlines)
    sz = FT.fileSize(testfile)
    assert sz == 13


def test_sizeof_fmt():
    """sizeof_fmt test."""
    got = FT.sizeof_fmt(6445440)
    assert got == "6.1MB"


def test_getFileHash():
    """getFileHash test."""
    fhash, fsize = FT.getFileHash(testfile)
    assert (
        fhash == "181d226b4a56b29a8ace235df83c9b0758a9decb4d6a45d0a567a6ddd1e1c970"
        and fsize == 13
    )


def test_readFile():
    """readFile test."""
    xstr = ""
    for line in testlines:
        xstr += line
    fcontent = FT.readFile(testfile)
    assert xstr == fcontent


def test_cleanup():
    """cleanup after testing."""
    FT.fileDelete(testfile)
    FT.fileDelete(renamefile)
    assert FT.fileExists(testfile) is False and FT.fileExists(renamefile) is False
