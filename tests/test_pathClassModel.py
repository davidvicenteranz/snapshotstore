import sys
from pathlib import Path
from unittest import TestCase

from snapshotstore.exceptions import PathNotExistsError, PathIsNotDir, PathIsNotWritable
from snapshotstore.models import PathClassModel
import os

TMP_PATH = '/tmp'
test_path = Path(os.getcwd()).joinpath('test_volume')
relative_path = './test_volume'

if not test_path.exists():
    test_path = Path(os.getcwd()).joinpath('tests').joinpath('test_volume')

if not Path(relative_path).exists():
    relative_path = './tests/test_volume'

print('test_path', test_path, file=sys.stderr)

class TestPathClassModel(TestCase):

    def test_check_path(self):
        path = PathClassModel.check_path(TMP_PATH)
        self.assertEqual(path, Path(TMP_PATH))
        self.assertTrue(path.exists())

    def test_non_exists_path(self):
        with self.assertRaises(PathNotExistsError) as context:
            path = PathClassModel.check_path('/myCrazy-InexistenT-paht')

    def test_file_as_path(self):
        with self.assertRaises(PathIsNotDir) as context:
            PathClassModel.check_path(Path(test_path).joinpath('this_file_is_not_a_dir'))

    def test_not_writeable_dir(self):
        with self.assertRaises(PathIsNotWritable) as context:
            PathClassModel.check_path(Path(test_path).joinpath('not_writable_dir'))

    def test_relative_path(self):
        """"Test chek_path returns absolute path"""
        self.assertFalse(Path(relative_path).is_absolute())
        self.assertTrue(PathClassModel.check_path(relative_path).is_absolute())

