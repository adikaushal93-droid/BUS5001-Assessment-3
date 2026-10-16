import subprocess
import sys

subprocess.run(
    [
        sys.executable, "-m", "pip", "install",
        "--upgrade",
        "--only-binary=:all:",
        "transformers>=4.51.3,<5",
        "accelerate>=1.6.0,<2"
    ],
    check=True
)

print("Installation completed successfully.")