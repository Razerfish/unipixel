# pylint: disable=missing-module-docstring
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []

setuptools.setup(
    name="unipixel",
    version="0.0.1",
    author="Fiona Wilson",
    author_email="fiona@razerfish.dev",
    description=("A testing utility for applications that would use the "
                 "adafruit-circuitpython-neopixel package"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/razerfish/unipixel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7"
    ],
    python_requires=">=3.5",
    install_requires=requirements,
    extras_require={
        'dev': [
            'autopep8',
            'nox',
            'pylint',
            'rope',
            'wheel',
        ],
        'lint': [
            'nox',
            'pylint',
        ]
    }
)
