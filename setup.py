from setuptools import setup


with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="dynamicTreeCut",
    version="0.1.1",
    packages=["dynamicTreeCut"],
    scripts=["dynamicTreeCut/df_apply.py", "dynamicTreeCut/R_func.py"],
    author="Kyle S. Smith",
    license="GPL-3 Licenses",
    description='Dynamic Tree Cut',
    install_requires=['numpy', 'scipy'],
    long_description=long_description,
    url="https://github.com/kylessmith/dynamicTreeCut",
    author_email="kyle.smith@stjude.org",
    )