# ccautils

a set of utilities for python3.6+ programmes and scripts.

<a name=headdd></a>
* [Install](#install)
* [Miscellaneous Utilities](#utils)
    * [Usage](#uusage)
* [File Utilities](#futils)
    * [Usage](#fusage)


<a name=install></a>
## [Install](#headdd)

Install for the user:
```
pip3 install ccautils --user
```

Install for a virtual environment:
```
pip install ccautils
```

<a name=utils></a>
## [Miscellaneous Utilities](#headdd)

<a name=uusage></a>
### [Usage](#headdd)

```
import ccautils.utils as UT
```

<a name=menu></a>
* [addToString](#addtostring)
* [delimitString](#delimitstring)
* [makeDictFromString](#makedictfromstring)
* [askMe](#askme)
* [padStr](#padstr)

<a name=addtostring></a>
### [addToString(xstr, xadd)](#menu)

Returns a string with `xadd` appended to `xstr`.  If `xadd` is a list, all
`str` members of the list will be appended in order.

```
UT.addToString("hello ", ["world"])

> "hello world"
```

<a name=delimitstring></a>
### [delimitString(xstr, xadd, delimeter=" - ")](#menu)

Constructs a string with `delimeter` between `xstr` and `xadd`.
If `xadd` is a list, all `str` members will be appended with the
`delimeter` inserted between them.

```
UT.delimitString("hello", ["bright", "world"], " ")

> "hello bright world"
```

<a name=makedictfromstring></a>
### [makeDictFromString(istr)](#menu)

Constructs a dictionary from a string of parameters. Leading and trailing
whitespace is stripped.

`istr` should be in the form `someparam=somevalue,someotherparam=otherval`

```
UT.makeDictFromString("sparam=sval, soparam = soval")

> {"sparam": "sval", "soparam": "soval"}
```

<a name=askme></a>
### [askMe(q, default)](#menu)

Requests input from the user.  Poses the question `q`. Returns the users
input or `default` if no input given.

```
UT.askMe("press 5, please", "8")

> press 5, please: 5
> 5
```

<a name=padstr></a>
### [padStr(xstr, xlen=2, pad=" ", padleft=True)](#menu)

Returns `xstr` `pad`ded to the required length, either on the
left (`padleft` is True) or the right (`padleft` is False)

```
UT.padStr("23", 5, "0")

> "00023"
```

<a name=futils></a>
## [File Utilities](#headdd)

<a name=fusage></a>
### [Usage](#headdd)

```
import ccautils.fileutils as FT
```
[modeline]: # ( vim: set ft=markdown tw=74 fenc=utf-8 spell spl=en_gb mousemodel=popup: )
