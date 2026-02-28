#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup script for aill. Follows amilib/encyclopedia pattern."""
from pathlib import Path
import re
from setuptools import setup

parent = Path(__file__).parent
with open(str(Path(parent, "aill", "__init__.py")), encoding="utf-8") as f:
    content = f.read()
version = re.search(r'__version__ = ["\']([^"\']+)["\']', content).group(1)

readme_path = Path(parent, "README.md")
readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else "aill: AILL prototype (OKFN/ClimateAcademy/SemanticClimate)."

setup(
    name="aill",
    version=version,
    description="Prototype for OKFN/ClimateAcademy/SemanticClimate AILL project",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="SemanticClimate team",
    url="https://github.com/semanticClimate/aill",
    packages=["aill"],
    package_dir={"aill": "aill"},
    include_package_data=True,
    install_requires=[],
    license="Apache License 2.0",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
