"""
llistplus - enhanced linked lists for Python
=============================================

This module provides doubly-linked lists (dllist) and singly-linked lists (sllist).
It automatically uses the fast C extension if available, or falls back to pure Python.
"""

from ._version import __version__

# Try to import the fast C extension first
try:
    from llistplus._llist import (
        dllist,
        dllistnode, 
        dllistiterator,
        dllistnodeiterator,
        sllist,
        sllistnode,
        sllistiterator,
        sllistnodeiterator
    )
    _c_extension = True
except ImportError:
    # Fall back to pure Python implementation
    import warnings
    warnings.warn(
        "C extension for llistplus not found, using pure Python implementation. "
        "For better performance, install the C extension.",
        ImportWarning
    )
    from ._pure import (
        dllist,
        dllistnode,
        dllistiterator, 
        dllistnodeiterator,
        sllist,
        sllistnode,
        sllistiterator,
        sllistnodeiterator
    )
    _c_extension = False

# For backward compatibility, expose as module-level attributes
__all__ = [
    'dllist', 'dllistnode', 'dllistiterator', 'dllistnodeiterator',
    'sllist', 'sllistnode', 'sllistiterator', 'sllistnodeiterator',
    '__version__'
]

def using_c_extension():
    """Return True if using the C extension, False if using pure Python."""
    return _c_extension
