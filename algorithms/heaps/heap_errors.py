

class HeapError(Exception):
    """Base class for heap errors."""
    pass


class NoParentError(HeapError):
    """Exception raised when trying to get the parent of the root node."""

    def __init__(self, msg='This node has no parent.'):
        self.msg = msg
