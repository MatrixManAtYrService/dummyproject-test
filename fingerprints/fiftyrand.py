import random
import subprocess
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description="fingerprint with fifty pseudorandom inputs"
)
parser.add_argument("projpath", help="a path to the repo under test")
args = parser.parse_args()

project_path = Path(args.projpath)
assert project_path.is_dir

random.seed(42)

for _ in range(50):
    inval = str(random.randint(-100000, 100000))
    script = str(project_path / "addone.sh")

    # writes to stdout, which the TDID dag aggregates as a fingerprint
    process = subprocess.run([script, inval])
