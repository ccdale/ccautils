"""Test file for fileutils.py file of ccautils module."""
import os

import pytest

import ccautils.fileutils as FT


testfile = os.environ.get("HOME") + "/testfile-deleteme"
ptestpath = "/tmp/ccautils-test-dir"
renamefile = os.path.dirname(testfile) + "/renamed-testfile-deleteme"
testlines = ["one\n", "two\n", "Three"]


def test_fileExists():
    """It exits True."""
    got = FT.fileExists(__file__)
    assert got is True


def test_fileExists_nonexist():
    """It exits False."""
    got = FT.fileExists("/non-existant")
    assert got is False


def test_fileExists_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.fileExists([])


def test_dirExists():
    """It exits True."""
    dird = os.path.dirname(__file__)
    got = FT.dirExists(dird)
    assert got is True


def test_dirExists_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.dirExists([])


def test_dfExists():
    """It exits True."""
    dird = os.path.dirname(__file__)
    got = FT.dfExists(dird)
    assert got is True


def test_dfExists_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.dfExists([])


def test_makePath():
    """It creates the ptestpath path"""
    FT.makePath(ptestpath)
    assert FT.dirExists(ptestpath) is True


def test_makePath_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.makePath([])


def test_makeFilePath():
    """It creates the directory structure for the testfile."""
    FT.makeFilePath(testfile)
    assert FT.dirExists(os.environ.get("HOME")) is True


def test_makeFilePath_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.makeFilePath([])


def test_absPath():
    """It expands `~` creating a fully-qualified file name."""
    tpath = "~/.bashrc"
    epath = os.environ.get("HOME") + "/.bashrc"
    got = FT.absPath(tpath)
    assert got == epath


def test_absPath_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.absPath([])


def test_fileTouch():
    """It creates the empty file and exits True."""
    FT.fileTouch(testfile)
    assert FT.fileExists(testfile) is True


def test_fileTouch_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.fileTouch([])


def test_rename():
    """It renames the test file and exits True."""
    FT.rename(testfile, renamefile)
    assert FT.fileExists(renamefile) is True


def test_rename_src_non_exist():
    """It raises an Exception."""
    with pytest.raises(Exception):
        FT.rename("wibble", "wobble")


def test_rename_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.rename([], "wibble")


def test_fileDelete():
    """It deletes the test file and exits False."""
    FT.fileDelete(renamefile)
    assert FT.fileExists(renamefile) is False


def test_fileDelete_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.fileTouch([])


def test_fileSize():
    """It computes the size of the file."""
    with open(testfile, "w") as ofn:
        ofn.writelines(testlines)
    sz = FT.fileSize(testfile)
    assert sz == 13


def test_fileSize_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.fileSize([])


def test_sizeof_fmt():
    """It displays the file size in human readable form."""
    got = FT.sizeof_fmt(6445440)
    assert got == "6.1MB"


def test_sizeof_fmt_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.sizeof_fmt([])


def test_getFileHash():
    """It computes the file's sha256 hash."""
    fhash, fsize = FT.getFileHash(testfile)
    assert (
        fhash == "181d226b4a56b29a8ace235df83c9b0758a9decb4d6a45d0a567a6ddd1e1c970"
        and fsize == 13
    )


def test_getFileHash_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.getFileHash([])


def test_readFile():
    """It sets the test string to be the content of the test file."""
    xstr = ""
    for line in testlines:
        xstr += line
    fcontent = FT.readFile(testfile)
    assert xstr == fcontent


def test_readFile_exception():
    """It raises a TypeError Exception."""
    with pytest.raises(TypeError):
        FT.readFile([])


def test_cleanup():
    """It cleans up the test files and exits False."""
    FT.fileDelete(testfile)
    FT.fileDelete(renamefile)
    assert FT.fileExists(testfile) is False and FT.fileExists(renamefile) is False
