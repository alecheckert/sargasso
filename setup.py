import os, setuptools
from pybind11.setup_helpers import Pybind11Extension, build_ext

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(PACKAGE_DIR, "src")
INC_DIR = os.path.join(PACKAGE_DIR, "include")

SRC_PATHS = list(map(lambda p: os.path.join(SRC_DIR, p), [
    "funcs.cpp",
    "module.cpp",
]))

ext_modules = [Pybind11Extension(
    "_sargasso",
    SRC_PATHS,
    include_dirs=[INC_DIR],
    cxx_std=14,
)]

setuptools.setup(
    name="sargasso",
    version="1.0",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    packages=["sargasso"],
)
