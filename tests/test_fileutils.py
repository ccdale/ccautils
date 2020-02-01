import os
import pytest
import ccautils.fileutils as FT


testfile = os.environ.get("HOME") + "/testfile-deleteme"
renamefile = os.path.dirname(testfile) + "/renamed-testfile-deleteme"
testlines = ["one\n", "two\n", "Three"]


def test_fileExists():
    got = FT.fileExists(__file__)
    assert got == True


def test_fileExists_nonexist():
    got = FT.fileExists("/non-existant")
    assert got == False


def test_dirExists():
    dird = os.path.dirname(__file__)
    got = FT.dirExists(dird)
    assert got == True


def test_dfExists():
    dird = os.path.dirname(__file__)
    got = FT.dfExists(dird)
    assert got == True


def test_absPath():
    tpath = "~/.bashrc"
    epath = os.environ.get("HOME") + "/.bashrc"
    got = FT.absPath(tpath)
    assert got == epath


def test_fileTouch():
    FT.fileTouch(testfile)
    assert True == FT.fileExists(testfile)


def test_rename():
    FT.rename(testfile, renamefile)
    assert True == FT.fileExists(renamefile)


def test_fileDelete():
    FT.fileDelete(renamefile)
    assert False == FT.fileExists(renamefile)


def test_fileSize():
    with open(testfile, "w") as ofn:
        ofn.writelines(testlines)
    sz = FT.fileSize(testfile)
    assert sz == 13


def test_sizeof_fmt():
    got = FT.sizeof_fmt(6445440)
    assert got == "6.1MB"


def test_getFileHash():
    fhash, fsize = FT.getFileHash(testfile)
    assert (
        fhash == "181d226b4a56b29a8ace235df83c9b0758a9decb4d6a45d0a567a6ddd1e1c970"
        and fsize == 13
    )


def test_readFile():
    xstr = ""
    for line in testlines:
        xstr += line
    fcontent = FT.readFile(testfile)
    assert xstr == fcontent


def test_cleanup():
    FT.fileDelete(testfile)
    FT.fileDelete(renamefile)
    assert FT.fileExists(testfile) == False and FT.fileExists(renamefile) == False
