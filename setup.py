#!/usr/bin/env python
from setuptools import setup, find_packages
from codecs import open

setup(
    name='whatsfly',
    version='0.0.1',
    license='MIT',
    author="Doy Bachtiar",
    author_email='blbblb669@gmail.com',
    url='https://github.com/cloned-doy/whatsfly',
    keywords='whatsfly',
    description="WhatsApp on the fly.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: WhatsApp :: WhatsApp Library",
        "Topic :: Software Development :: Libraries",
    ]
)