Introduction
============

ast2json is a small module that will convert any python AST node into its ast
representation formated in a JSON compatible python representation (list and
dicts containing string, ints and null).

Installation
============

::

    pip install ast2json
    # or to have lastest version
    pip install git+git://github.com/Psycojoker/ast2json.git

Usage
=====

::

    >>> import json
    >>> from ast import parse
    >>> from ast2json import ast2json

    >>> ast = ast2json(parse(open('some_python_source_file.py').read()))
    >>> print json.dumps(ast, indent=4)

If you are lazy, "str2json" will apply the "parse" method of ast on a string for you, so you'll be able to write:

::

    >>> str2json(open('some_python_source_file.py').read())

Example
=======

This is the result of converting 'print "Hello World!"' (and applying json.dumps on the result).

::

    {
        "body": [
            {
                "_type": "Print", 
                "nl": true, 
                "col_offset": 0, 
                "dest": null, 
                "values": [
                    {
                        "s": "Hello World!", 
                        "_type": "Str", 
                        "lineno": 1, 
                        "col_offset": 6
                    }
                ], 
                "lineno": 1
            }
        ], 
        "_type": "Module"
    }


Changelog
=========

0.2 (2016-09-03)
----------------

* python 3 support and some unit testing by Juncheol Cho @zironycho

Licence
=======

BSD
