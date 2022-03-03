# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/main/LICENSE
# Copyright (c) https://github.com/PyCQA/astroid/graphs/contributors
import enum
import platform
import sys

PY36 = sys.version_info[:2] == (3, 6)
PY38 = sys.version_info[:2] == (3, 8)
PY37_PLUS = sys.version_info >= (3, 7)
PY38_PLUS = sys.version_info >= (3, 8)
PY39_PLUS = sys.version_info >= (3, 9)
PY310_PLUS = sys.version_info >= (3, 10)
BUILTINS = "builtins"  # TODO Remove in 2.8

WIN32 = sys.platform == "win32"

IMPLEMENTATION_PYPY = platform.python_implementation() == "PyPy"


class Context(enum.Enum):
    Load = 1
    Store = 2
    Del = 3


# TODO Remove in 3.0 in favor of Context
Load = Context.Load
Store = Context.Store
Del = Context.Del
