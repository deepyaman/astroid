# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/main/LICENSE
# Copyright (c) https://github.com/PyCQA/astroid/graphs/contributors

"""Every available node class.

.. seealso::
    :doc:`ast documentation <green_tree_snakes:nodes>`

All nodes inherit from :class:`~astroid.nodes.node_classes.NodeNG`.
"""

# Nodes not present in the builtin ast module:  DictUnpack, Unknown, and EvaluatedObject.

from astroid.nodes.node_classes import (  # pylint: disable=redefined-builtin (Ellipsis)
    CONST_CLS,
    AnnAssign,
    Arguments,
    Assert,
    Assign,
    AssignAttr,
    AssignName,
    AsyncFor,
    AsyncWith,
    Attribute,
    AugAssign,
    Await,
    BaseContainer,
    BinOp,
    BoolOp,
    Break,
    Call,
    Compare,
    Comprehension,
    Const,
    Continue,
    Decorators,
    DelAttr,
    Delete,
    DelName,
    Dict,
    DictUnpack,
    Ellipsis,
    EmptyNode,
    EvaluatedObject,
    ExceptHandler,
    Expr,
    ExtSlice,
    For,
    FormattedValue,
    Global,
    If,
    IfExp,
    Import,
    ImportFrom,
    Index,
    JoinedStr,
    Keyword,
    List,
    Match,
    MatchAs,
    MatchCase,
    MatchClass,
    MatchMapping,
    MatchOr,
    MatchSequence,
    MatchSingleton,
    MatchStar,
    MatchValue,
    Name,
    NamedExpr,
    NodeNG,
    Nonlocal,
    Pass,
    Pattern,
    Raise,
    Return,
    Set,
    Slice,
    Starred,
    Statement,
    Subscript,
    TryExcept,
    TryFinally,
    Tuple,
    UnaryOp,
    Unknown,
    While,
    With,
    Yield,
    YieldFrom,
    are_exclusive,
    const_factory,
    unpack_infer,
)
from astroid.nodes.scoped_nodes import (
    AsyncFunctionDef,
    ClassDef,
    ComprehensionScope,
    DictComp,
    FunctionDef,
    GeneratorExp,
    Lambda,
    ListComp,
    LocalsDictNodeNG,
    Module,
    SetComp,
    builtin_lookup,
    function_to_method,
    get_wrapping_class,
)
from astroid.nodes.utils import Position

_BaseContainer = BaseContainer  # TODO Remove for astroid 3.0

ALL_NODE_CLASSES = (
    _BaseContainer,
    BaseContainer,
    AnnAssign,
    Arguments,
    Assert,
    Assign,
    AssignAttr,
    AssignName,
    AsyncFor,
    AsyncFunctionDef,
    AsyncWith,
    Attribute,
    AugAssign,
    Await,
    BinOp,
    BoolOp,
    Break,
    Call,
    ClassDef,
    Compare,
    Comprehension,
    ComprehensionScope,
    Const,
    const_factory,
    Continue,
    Decorators,
    DelAttr,
    Delete,
    DelName,
    Dict,
    DictComp,
    DictUnpack,
    Ellipsis,
    EmptyNode,
    EvaluatedObject,
    ExceptHandler,
    Expr,
    ExtSlice,
    For,
    FormattedValue,
    FunctionDef,
    GeneratorExp,
    Global,
    If,
    IfExp,
    Import,
    ImportFrom,
    Index,
    JoinedStr,
    Keyword,
    Lambda,
    List,
    ListComp,
    LocalsDictNodeNG,
    Match,
    MatchAs,
    MatchCase,
    MatchClass,
    MatchMapping,
    MatchOr,
    MatchSequence,
    MatchSingleton,
    MatchStar,
    MatchValue,
    Module,
    Name,
    NamedExpr,
    NodeNG,
    Nonlocal,
    Pass,
    Pattern,
    Raise,
    Return,
    Set,
    SetComp,
    Slice,
    Starred,
    Subscript,
    TryExcept,
    TryFinally,
    Tuple,
    UnaryOp,
    Unknown,
    While,
    With,
    Yield,
    YieldFrom,
)

__all__ = (
    "AnnAssign",
    "are_exclusive",
    "Arguments",
    "Assert",
    "Assign",
    "AssignAttr",
    "AssignName",
    "AsyncFor",
    "AsyncFunctionDef",
    "AsyncWith",
    "Attribute",
    "AugAssign",
    "Await",
    "BinOp",
    "BoolOp",
    "Break",
    "builtin_lookup",
    "Call",
    "ClassDef",
    "CONST_CLS",
    "Compare",
    "Comprehension",
    "ComprehensionScope",
    "Const",
    "const_factory",
    "Continue",
    "Decorators",
    "DelAttr",
    "Delete",
    "DelName",
    "Dict",
    "DictComp",
    "DictUnpack",
    "Ellipsis",
    "EmptyNode",
    "EvaluatedObject",
    "ExceptHandler",
    "Expr",
    "ExtSlice",
    "For",
    "FormattedValue",
    "FunctionDef",
    "function_to_method",
    "GeneratorExp",
    "get_wrapping_class",
    "Global",
    "If",
    "IfExp",
    "Import",
    "ImportFrom",
    "Index",
    "JoinedStr",
    "Keyword",
    "Lambda",
    "List",
    "ListComp",
    "LocalsDictNodeNG",
    "Match",
    "MatchAs",
    "MatchCase",
    "MatchClass",
    "MatchMapping",
    "MatchOr",
    "MatchSequence",
    "MatchSingleton",
    "MatchStar",
    "MatchValue",
    "Module",
    "Name",
    "NamedExpr",
    "NodeNG",
    "Nonlocal",
    "Pass",
    "Position",
    "Raise",
    "Return",
    "Set",
    "SetComp",
    "Slice",
    "Starred",
    "Statement",
    "Subscript",
    "TryExcept",
    "TryFinally",
    "Tuple",
    "UnaryOp",
    "Unknown",
    "unpack_infer",
    "While",
    "With",
    "Yield",
    "YieldFrom",
)
