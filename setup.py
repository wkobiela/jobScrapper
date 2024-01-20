#!/usr/bin/env python
"""This module contains setup instructions for jobscrapper."""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
    
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ""

setup(
    name="jobscrapper",
    version='0.0.1',
    author="wkobiela",
    author_email="test@test.com",
    packages=find_packages(),
    package_data={"": ["LICENSE"],},
    url="https://github.com/wkobiela/jobScrapper",
    license="GNU General Public License",
    entry_points={
        "console_scripts": [
            "jobscrapper=jobscrapper.run:main"
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: GNU General Public License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    description=("jobScrapper -  Simplify your IT job search."),
    long_description=long_description,
    include_package_data=True,
    long_description_content_type="text/markdown",
    zip_safe=False,
    platforms='any',
    python_requires=">=3.9",
    project_urls={
        "Bug Reports": "https://github.com/wkobiela/jobScrapper/issues",
    },
    install_requires=[
    'beautifulsoup4',
    'openpyxl',
    'pandas',
    'Requests',
    'unidecode',
    'XlsxWriter' 
    ],
    keywords=["work", "it", "search", "scrapper",],
)