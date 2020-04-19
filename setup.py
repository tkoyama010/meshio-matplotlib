from setuptools import setup

setup(
    name="meshioplt",
    version="0.0.1",
    install_requires=["meshio", "matplotlib"],
    packages=["meshioplt"],
    package_dir={"meshioplt": "meshioplt"},
)
