"""
Tests for aill.util. Style: assert (not return False), descriptive messages, no mocks.
"""
from pathlib import Path

from aill.util import get_version
from test.resources import Resources


def test_get_version_returns_string():
    """get_version() returns a non-empty string."""
    result = get_version()
    assert result is not None, "get_version() should not return None"
    assert isinstance(result, str), f"get_version() should return str, got {type(result)}"
    assert len(result) > 0, f"get_version() should return non-empty string, got {result!r}"


def test_resources_temp_dir_is_path():
    """Resources.TEMP_DIR is a Path under project temp."""
    temp_dir = Resources.TEMP_DIR
    assert temp_dir is not None, "Resources.TEMP_DIR should be set"
    assert isinstance(temp_dir, Path), f"TEMP_DIR should be Path, got {type(temp_dir)}"
    assert temp_dir.name == "temp", f"TEMP_DIR should end with 'temp', got {temp_dir}"


def test_temp_dir_construction_style():
    """Temp subpaths use Path(Resources.TEMP_DIR, ...) per style guide."""
    subdir = Path(Resources.TEMP_DIR, "test", "test_util", "test_temp_dir_construction_style")
    assert subdir.parent == Path(Resources.TEMP_DIR, "test", "test_util"), (
        f"subdir parent should be temp/test/test_util, got {subdir.parent}"
    )
