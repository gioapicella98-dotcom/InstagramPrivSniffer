# Helper: check and install "instapvsnifffer"
# Quick manual steps (Windows / macOS & Linux)
# 1) Create venv:
#    python -m venv .venv
# 2) Activate:
#    Windows: .venv\Scripts\activate
#    macOS/Linux: source .venv/bin/activate
# 3) Check package availability:
#    pip index versions instapvsnifffer   # or: pip search instapvsnifffer
# 4) Install:
#    pip install instapvsnifffer
# 5) Verify:
#    pip show instapvsnifffer
#    python -c "import instapvsnifffer; print(instapvsnifffer.__version__)"
# If pip cannot find the package, check for a GitHub repo and install from source:
#    pip install git+https://github.com/<owner>/<repo>.git

# Small automated script (run inside your activated venv)
import subprocess
import sys

def run(cmd):
    print(">", " ".join(cmd))
    subprocess.check_call(cmd)

def main(pkg="instapvsnifffer"):
    try:
        # Try to show package info (will raise if not installed)
        run([sys.executable, "-m", "pip", "show", pkg])
        print(f"{pkg} appears to be already installed.")
    except subprocess.CalledProcessError:
        print(f"{pkg} not installed — attempting to install from PyPI...")
        try:
            run([sys.executable, "-m", "pip", "install", pkg])
            run([sys.executable, "-m", "pip", "show", pkg])
            # quick import check
            run([sys.executable, "-c", f"import {pkg}; print(getattr({pkg}, '__version__', 'no __version__'))"])
        except subprocess.CalledProcessError as e:
            print("Install failed. If the package name is incorrect or not on PyPI, check the project's GitHub and install via:")
            print("  pip install git+https://github.com/<owner>/<repo>.git")
            raise SystemExit(1)

if __name__ == "__main__":
    # Usage: run this file after activating a venv: python Untitled-1
    main()