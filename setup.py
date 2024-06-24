#!/usr/bin/env python
"""This module contains setup instructions for jobscrapper."""

from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="jobscrapper",
    version='0.0.10',
    author="wkobiela",
    author_email="wiktor.kobiela@gmail.com",
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
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
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
    'selenium',
    'unidecode',
    'XlsxWriter' 
    ],
    keywords=["work", "it", "search", "scrapper",],
)
