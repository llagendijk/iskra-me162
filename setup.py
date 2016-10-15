#!/usr/bin/python
import os
from distutils.core import setup

def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read

setup(  name='iskra-me162',
        version='0.1.0',
        description="Script that feeds ME162 readings as a P1 meter to Domoticz",
        license="GPLv3",
        long_description=read("README.rst"),
        author='Louis Lagendijk',
        author_email='louis.lagendijk@gmail.com',
        scripts = ["iskra-me162"],
	data_files = [("/etc/default", ["iskra-me162.config"]),
		      ("/etc/systemd/system", ["iskra-me162.service"]),
		     ],
	url = "https://github.com/llagendijk/iskra-me162.git",
        classifiers = [
                "Environment :: No Input/Output (Daemon)",
                "Development Status :: 4 - Beta",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        ],
)

