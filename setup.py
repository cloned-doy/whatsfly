#!/usr/bin/env python
from setuptools import setup, find_packages
from codecs import open

setup(
    name='whatsfly',
    version='0.0.22',
    license='MIT',
    author="Doy Bachtiar",
    author_email='adityabachtiar996@gmail.com',
    url='https://github.com/cloned-doy/whatsfly',
    keywords='whatsfly',
    description="WhatsApp on the fly.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",    
        "Programming Language :: Python :: 3",    
        "Environment :: Web Environment",    
        "Topic :: Communications",    
        "Topic :: Communications :: Chat",    
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)

