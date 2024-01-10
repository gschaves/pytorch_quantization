from setuptools import setup, find_packages

VERSION_FILE = "version.py"
INIT_FILE = "pytorch_quantization/__init__.py"

def get_version():
    with open(VERSION_FILE, encoding="utf-8") as f:
        ver = f.readline()

    if ver.startswith("for"):
        with open(INIT_FILE, encoding="utf-8") as f:
            for line in f.readlines():
                if line.startswith("__version__"):
                    ver = line.split()[-1].strip('"') + "+master"

    return ver

setup(
    name='pytorch-quantization',
    version=get_version(),
    packages=find_packages(where="./pytorch_quantization")
)
