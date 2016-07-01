import sys

if sys.version_info.major == 2:
    BUILTIN_PURE = (int, basestring, float, long, bool)
    BUILTIN_BYTES = (bytearray, bytes)
else:
    BUILTIN_PURE = (int, str, float, bool)
    BUILTIN_BYTES = (bytearray, bytes)

