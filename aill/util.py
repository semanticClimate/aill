#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Minimal utilities for aill. Follows amilib style: absolute imports, Path with multiple args.
"""
from pathlib import Path


def get_version():
    """Return package version string."""
    from aill import __version__
    return __version__
