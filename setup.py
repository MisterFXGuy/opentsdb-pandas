
from setuptools import setup, find_packages

NAME        = "opentsdb_pandas"
VERSION     = "0.0.1"
URL         = "https://github.com/metrilyx/" + NAME
DESCRIPTION = "Library to convery OpenTSDB data to pandas datastructures."

INSTALL_REQUIRES = [ p for p in open('requirements.txt').read().split('\n') if p != '' and not p.startswith('#') ]

setup(
    name=NAME,
    version=VERSION,
    url=URL,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    author='euforia',
    author_email='euforia@gmail.com',
    license="GPL",
    setup_requires=["numpy"],
    install_requires=INSTALL_REQUIRES,
    packages=["opentsdb_pandas"]
)
