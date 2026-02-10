from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lennys-wisdom-mcp",
    version="2.0.0",
    author="Edison Cruz",
    author_email="edisoncruz@gmail.com",
    description="MCP server providing structured access to wisdom from Lenny's Podcast",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edisoncruz/lennys-wisdom-mcp",
    packages=find_packages(),
    package_data={
        'lennys_wisdom': ['data/episodes/*.json'],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Product Teams",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "fastmcp>=0.1.0",
    ],
    entry_points={
        'console_scripts': [
            'lennys-wisdom=lennys_wisdom.__main__:main',
        ],
    },
)
