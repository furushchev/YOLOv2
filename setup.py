#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp>


from distutils.core import setup
from setuptools import find_packages
from distutils.extension import Extension

setup(
    name="yolov2",
    version=open("VERSION").readline()[0],
    description="Chainer implementation for YOLO v2 object detection",
    long_description=open("README.md").read(),
    author="Yuki Furuta",
    author_email="furushchev@jsk.imi.i.u-tokyo.ac.jp",
    license="YOLO",
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    install_requires=open("requirements.txt").readlines(),
    keywords="machine-learning",
)
