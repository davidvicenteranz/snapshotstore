from pathlib import Path
from unittest import TestCase
from snapshotstore.models import StoreBase

from .config import TMP_PATH, test_path, relative_path

class TestStoreBase(TestCase):
    def test__init__(self):
        self.assertTrue(isinstance(StoreBase('.').path, Path))
        self.assertEqual(StoreBase('.').path, Path('.').absolute())
        self.assertTrue(StoreBase('.').path.exists())
        Path('.').is_block_device()