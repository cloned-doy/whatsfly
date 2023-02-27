#!/usr/bin/env python
from setuptools import setup, find_packages, Extension
from codecs import open
import glob
import os

data_files = []
directories = glob.glob('whatsfly/dependencies/')
for directory in directories:
    files = glob.glob(directory+'*')
    data_files.append(('whatsfly/dependencies', files))

# about = {}
# here = os.path.abspath(os.path.dirname(__file__))
# with open(os.path.join(here, "whatsfly", "__version__.py"), "r", "utf-8") as f:
#     exec(f.read(), about)

setup(
    name='whatsfly',
    version='0.0.0',
    license='MIT',
    author="Doy Bachtiar",
    author_email='blbblb669@gmail.com',
    url='https://github.com/cloned-doy/whatsfly',
    keywords='whatsfly',
    install_requires=[
          'requests',
      ],
    description="WhatsApp on the fly.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*'],
    },
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ]
)

