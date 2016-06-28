import sys


if sys.version_info.major == 2:
    BUILTIN_TYPES = (int, basestring, float, long, complex, bool)
else:
    BUILTIN_TYPES = (int, str, float, complex, bool)
