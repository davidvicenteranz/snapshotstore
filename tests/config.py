import os
import sys
from pathlib import Path
import tempfile

TMP_PATH = tempfile.gettempdir()
test_path = Path(os.getcwd()).joinpath('test_volume')
relative_path = './test_volume'

if not test_path.exists():
    test_path = Path(os.getcwd()).joinpath('tests').joinpath('test_volume')

if not Path(relative_path).exists():
    relative_path = './tests/test_volume'

print('test_path', test_path, file=sys.stderr)