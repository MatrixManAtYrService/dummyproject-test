import random
import subprocess
import argparse
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description="can addone.sh increment a negative integer?")
parser.add_argument('projpath', help="a path to the repo under test")
args = parser.parse_args()

project_path = Path(args.projpath)
assert project_path.is_dir

script = str(project_path / 'addone.sh')
process = subprocess.run([script, "-100"], stdout=subprocess.PIPE).stdout

result = int(process)
expect = -99
if result != expect:
    raise ValueError(f"expected {expect}. got {result}")
    # will exit nonzero and signal to tdid dag that this test failed
    
sys.exit(0) # signal to tdid dag that this test passed