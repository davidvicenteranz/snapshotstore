from pathlib import Path
from unittest import TestCase
import os
from snapshotstore.exceptions import PathNotExistsError, PathIsNotDir, PathIsNotWritable, PathIsNotReadable
from snapshotstore.models import PathClassModel
from .config import TMP_PATH, test_path, relative_path

files = result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(test_path) for f in filenames]

class TestPathClassModel(TestCase):

    def test_check_path(self):
        path = PathClassModel.check_path(TMP_PATH)
        self.assertTrue(isinstance(path, Path))
        self.assertEqual(path, Path(TMP_PATH))
        self.assertTrue(path.exists())

    def test_non_exists_path(self):
        with self.assertRaises(PathNotExistsError) as context:
            path = PathClassModel.check_path('/myCrazy-InexistenT-paht')

    def test_file_as_path(self):
        with self.assertRaises(PathIsNotDir) as context:
            PathClassModel.check_path(Path(test_path).joinpath('this_file_is_not_a_dir'))

    def test_not_writable_dir(self):
        from stat import S_IREAD
        not_writable_path = str(Path(relative_path).joinpath('not_writable_dir').absolute())
        # Create only readable dir to test
        os.mkdir(not_writable_path, S_IREAD)
        self.assertFalse(Path(relative_path).is_absolute())
        self.assertTrue(PathClassModel.check_path(relative_path).is_absolute())
        with self.assertRaises(PathIsNotWritable) as context:
            PathClassModel.check_path(not_writable_path)
        os.chmod(not_writable_path, mode=7777)
        os.removedirs(not_writable_path)

    def test_not_readble_dir(self):
        from stat import S_IWRITE
        not_writable_path = str(Path(relative_path).joinpath('not_readable_dir').absolute())
        # Create only writable dir to test
        os.mkdir(not_writable_path, S_IWRITE)
        self.assertFalse(Path(relative_path).is_absolute())
        self.assertTrue(PathClassModel.check_path(relative_path).is_absolute())
        with self.assertRaises(PathIsNotReadable) as context:
            PathClassModel.check_path(not_writable_path)
        os.chmod(not_writable_path, mode=7777)
        os.removedirs(not_writable_path)

    def test_relative_path(self):
        """"Test chek_path returns absolute path"""
        self.assertEqual(str(PathClassModel.check_path('.')), os.getcwd())
        self.assertTrue(isinstance(PathClassModel.check_path('.'), Path))


    def test__soft_link(self):
        """Ensures path is not symlink and is an abcolute path"""
        from stat import S_IWRITE, S_IREAD
        real_path = str(Path(test_path).joinpath('real_path').absolute())
        not_real_path = str(Path(test_path).joinpath('not_real_path').absolute())

        os.mkdir(real_path, S_IWRITE | S_IREAD)
        self.assertFalse(Path(real_path).is_symlink())
        os.symlink(real_path, not_real_path, target_is_directory=True)
        self.assertTrue(Path(not_real_path).is_symlink())

        # Ensures path is the real path
        self.assertEqual(PathClassModel.check_path(not_real_path).absolute(), Path(real_path).absolute())

        os.remove(not_real_path)
        self.assertFalse(Path(not_real_path).exists())
        os.removedirs(real_path)