import os
from pathlib import Path
"""
datastore
    |
    ---- > namespace
               |
               -------> timestamp / timestamp_index
               |             |
               |             ----> /last/{hash}
               |                   /first/{hash}
               |                   /{key}/{hash}
               |                   /__meta__/count/{count}
               |
               |
               -------> key / key_index
                        |
                        ----> /last/timestamp/{hash}
                        ----> /first/{hash}
                        ----> /{timestamp}/{hash}
                        ----> /__meta__/count/count}
"""

class PathClassModel:
    path : Path
    id : str

    @staticmethod
    def check_path(path: str, raise_on_not_exists=True):
        """Check if path is usable. Must exists, be a directory and writeable by this instance."""
        path = Path(path)
        if not path.exists() and raise_on_not_exists:
            raise RuntimeError(f'Path {path} does not exist.')
        if not path.is_dir():
            raise RuntimeError(f'Path {path} is not a directory.')
        if raise_on_not_exists and path.exists() and not os.access(path, os.W_OK):
            raise RuntimeError(f'Path {path} exists, but is not writeable.')

        if path.is_absolute():
            return path

        return path.absolute()

    @staticmethod
    def makedirs(path : str):
        Path(path).mkdir()


class VersionBase(PathClassModel):
    hash : str
    content : any
    is_binary : bool
    is_object : bool
    is_file: bool
    timestamp: int

    def __init__(self, path, content=None, binary=False, object=False, is_file=False):
        self.__hash = None
        self.path = path
        self.content = content
        self.is_binary = binary
        self.is_object = object
        self.is_file = is_file

    @property
    def hash(self):
        if self.__hash:
            return self.__hash

class SnapshotBase:
    def __init__(self, snapshot: str):
        self.path = Path(snapshot)

    @property
    def versions(self):
        """Return a list of versions this snapshot."""

    def Version(self, path) -> VersionBase:
        return VersionBase(path)

class NamespaceBase(PathClassModel):
    def __init__(self, namespace: str):
        self.path = Path(namespace)

    def Snapshot(self, id)->[SnapshotBase]:
        return SnapshotBase(self, self.path.joinpath(id))

    def snapshots(self) ->[SnapshotBase]:
        """Return a list of snapshots."""
        pass

class StoreBase(PathClassModel):
    """Represents a basic Store object."""
    path: Path


    def __init__(self, path: str):
        """Store Initialization.

        Args:
            path (str): A writable path as string.
        """
        self.path = self.check_path(path)

    def Namespace(self, string:str)->NamespaceBase:
        return NamespaceBase(self.path.joinpath(string))


    def namespaces(self) -> [NamespaceBase]:
        pass


