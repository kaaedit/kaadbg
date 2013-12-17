import os, sys
from setuptools import setup, find_packages, Extension

def read(fname):
    return open(
            os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "kaadbg",
    version = "0.2.0",
    description='Remote debugger runner for kaa',
    url='https://github.com/kaaedit/kaadbg',
    author='Atsuo Ishimoto',
    author_email='ishimoto@gembook.org',
    long_description=read('README.rst'),
    classifiers=[
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Development Status :: 3 - Alpha",
            "Topic :: Text Editors",
            "Topic :: Software Development :: Debuggers",
            "Environment :: Console :: Curses",
            "License :: OSI Approved :: MIT License", ],
    license='MIT License',
    packages = find_packages(),
)
