from setuptools import setup
from Cython.Build import cythonize

setup(
    name="dalekcam_modules",
    ext_modules=cythonize("dalekcam_modules.pyx"),
    zip_safe=False,
)