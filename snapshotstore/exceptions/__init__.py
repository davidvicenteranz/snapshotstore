class PathNotExistsError(Exception):
    """Raises when path not exists"""
    pass

class PathIsNotDir(Exception):
    """Raises when gicen path is a file an not dir."""
    pass

class PathIsNotWritable(Exception):
    """Raises when path is not writeable."""

class PathIsNotReadable(Exception):
    """Raises when path is not writeable."""