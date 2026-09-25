import unittest


class TrialTests(unittest.TestCase):
    def test_readme_exists(self) -> None:
        from pathlib import Path
        self.assertTrue(Path("README.md").exists())
