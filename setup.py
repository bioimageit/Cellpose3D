import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("gitpython")

from git import Repo

Repo.clone_from("https://github.com/stegmaierj/Cellpose3D.git", "./Cellpose3D")