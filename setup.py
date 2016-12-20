from setuptools import setup

setup(name='hue-python-rgb-converter',
    description='RGB conversion tool written in Python for Philips Hue',
    author='Benjamin Knight',
    version="1.0",
    package-dir={'': 'rgb_xy'},
    packages=['rgb_xy'],
    install_requires=[],
)
