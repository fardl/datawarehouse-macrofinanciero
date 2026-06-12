
import sys
import subprocess

result = subprocess.run(
    [
        sys.executable,
        "etl/load_staging.py"
    ],
    check=True
)

