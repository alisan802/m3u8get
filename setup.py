# Author: Tomohiro Arikita <alisan802@proton.me>
# Copyright (c) 2024 Tomohiro Arikita
# Licence: MIT

from setuptools import setup

DESCRIPTION = 'm3u8get: Get m3u8 video file.'
NAME = 'm3u8get'
AUTHOR = 'Tomohiro Arikita'
AUTHOR_EMAIL = 'alisan802@proton.me'
URL = '' '''ToDo'''
LICENSE = 'MIT'
DOWNLOAD_URL = URL
VERSION = '0.1.0'
PYTHON_REQUIRES = '>=3.8'
INSTALL_REQUIRES = [
    'requests>=2.31.0'
]
PACKAGES = [
    'm3u8get'
]
PACKAGE_DIR = {
    '': 'src'
}
KEYWORDS = 'm3u8 video download'
CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8'
]
with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    package_dir=PACKAGE_DIR,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES
)
