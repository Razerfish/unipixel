# pylint: disable=missing-module-docstring
import setuptools


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

REQUIREMENTS = []

setuptools.setup(
    name="unipixel",
    version="0.0.1",
    author="Fiona Wilson",
    author_email="fiona@razerfish.dev",
    description=("A testing utility for applications that would use the "
                 "adafruit-circuitpython-neopixel package"),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/razerfish/unipixel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={
        "Source Code": "https://github.com/Razerfish/unipixel",
        "Bug Tracker": "https://github.com/Razerfish/unipixel/issues"
    },
    python_requires=">=3.5",
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'autopep8>=1.5',
            'nox>=2019.11.9',
            'pylint>=2.4.0',
            'rope>=0.16.0',
            'twine>=3.1.0'
        ],
        'lint': [
            'nox>=2019.11.9',
            'pylint>=2.4.0',
        ]
    }
)
