from setuptools import setup, find_packages

VERSION = "1.0.0"

with open("requirements.txt") as f:
    requirements = [l.strip() for l in f.readlines()]

setup(
    name="text-normalize",
    author="vcokltfre",
    url="https://github.com/vcokltfre/normalize",
    version=VERSION,
    packages=find_packages(),
    license="MIT",
    description="Normalize text to remove unicode lookalike characters.",
    install_requires=requirements,
)
