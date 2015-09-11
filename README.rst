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

    >>> from ast import parse
    >>> from ast2json import ast2json

    >>> print(ast2json(parse(open('some_python_source_file.py').read(), indent=4))

If you want just the dict use:

::
    >>> from ast2json import ast2dict
    >>> str2dict(open('some_python_source_file.py').read())

Example
=======

This is the result of converting 'print("Hello World!")'.

::

    {
        "body": [
            {
                "node_type": "Print", 
                "nl": true, 
                "col_offset": 0, 
                "dest": null, 
                "values": [
                    {
                        "s": "Hello World!", 
                        "node_type": "Str", 
                        "lineno": 1, 
                        "col_offset": 6
                    }
                ], 
                "lineno": 1
            }
        ], 
        "node_type": "Module"
    }


Licence
=======

BSD
