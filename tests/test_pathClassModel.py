from pathlib import Path
from unittest import TestCase
from snapshotstore.models import PathClassModel

TMP_PATH = '/tmp'

class TestPathClassModel(TestCase):

    def test_check_path(self):
        path = PathClassModel.check_path(TMP_PATH)
        self.assertEqual(path, Path(TMP_PATH))
        self.assertTrue(path.exists())

    def test_non_exists_path(self):
        with self.assertRaises(RuntimeError) as context:
            path = PathClassModel.check_path('/myCrazy-InexistenT-paht')


