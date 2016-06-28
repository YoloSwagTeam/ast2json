import sys

if sys.version_info.major == 2:
    from ast2json import *
    BUILTIN_TYPES = (int, basestring, float, long, complex, bool)
else:
    from ast2json.ast2json import *
    BUILTIN_TYPES = (int, str, float, complex, bool)
