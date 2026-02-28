"""
Test resources and paths for aill. Follows amilib style (Resources.TEMP_DIR, Path with multiple args).
"""
from pathlib import Path

# Test data (shipped with package)
TEST_RESOURCES_DIR = Path(Path(__file__).parent, "resources")
assert TEST_RESOURCES_DIR.name == "resources", f"{TEST_RESOURCES_DIR.name} should be 'resources'"

# Temporary output (not in repo). Use Path(Resources.TEMP_DIR, "test", module, class) in tests.
TEMP_DIR = Path(Path(__file__).parent.parent, "temp")


class Resources:
    """
    Paths for tests and temp output.
    TEMP_DIR: per-test/output (not committed). Use subdirs like test/<module>/<class>.
    """
    TEST_RESOURCES_DIR = TEST_RESOURCES_DIR
    TEMP_DIR = TEMP_DIR
