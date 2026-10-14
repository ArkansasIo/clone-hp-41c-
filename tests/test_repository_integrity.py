"""Fast, dependency-free checks for the Nonpareil source repository.

These tests intentionally check source-tree integrity only. They do not claim
that the legacy simulator compiles or that calculator behavior is correct.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RepositoryIntegrityTests(unittest.TestCase):
    def test_core_project_files_exist(self):
        for relative in (
            "README",
            "INSTALL",
            "COPYING",
            "CREDITS",
            "SConstruct",
            "src",
            "ncd",
            "nui",
            "scons",
            "dtd",
            "LICENSES",
        ):
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).exists(), relative)

    def test_license_texts_are_present(self):
        for relative in (
            "LICENSES/GPL-2.txt",
            "LICENSES/GPL-3.0.txt",
            "LICENSES/CC-BY-SA-3.0.txt",
        ):
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)

    def test_hp41_family_inputs_exist(self):
        for relative in (
            "ncd/41c/SConscript",
            "ncd/41c/41cv.ncd.tmpl",
            "ncd/41c/41cx.ncd.tmpl",
            "nui/nut/41c",
        ):
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).exists(), relative)

    def test_scons_entry_point_mentions_source_build(self):
        text = (ROOT / "SConstruct").read_text(encoding="utf-8")
        self.assertIn("src/SConscript", text)
        self.assertIn("ncd/SConscript", text)
        self.assertIn("scons/ncd.py", text)

    def test_docs_do_not_claim_behavioral_coverage(self):
        text = (ROOT / "docs/PROJECT_ARCHITECTURE.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("does not claim", text)
        self.assertIn("Behavioral validation", text)


if __name__ == "__main__":
    unittest.main()
