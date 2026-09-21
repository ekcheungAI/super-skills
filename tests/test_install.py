import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)

class InstallTests(unittest.TestCase):
    def test_dry_run_does_not_create_destination(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "skills"
            self.assertEqual(installer.install(dest), 5)
            self.assertFalse(dest.exists())

    def test_complete_copy_and_conflict_preserves_existing_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "skills"
            installer.install(dest, True)
            for name in installer.NAMES:
                source = ROOT / "skills" / name
                for p in source.rglob("*"):
                    if p.is_file():
                        self.assertEqual(p.read_bytes(), (dest / name / p.relative_to(source)).read_bytes())
            marker = dest / "superadhd" / "student-note.txt"
            marker.write_text("keep me")
            with self.assertRaises(ValueError):
                installer.install(dest, True)
            self.assertEqual(marker.read_text(), "keep me")

    def test_late_conflict_writes_no_earlier_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            (dest / "superloop").mkdir()
            with self.assertRaises(ValueError):
                installer.install(dest, True)
            self.assertEqual([p.name for p in dest.iterdir()], ["superloop"])

    def test_broken_symlink_conflict_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            (dest / "superpersona").symlink_to(dest / "missing")
            with self.assertRaises(ValueError):
                installer.install(dest, True)
            self.assertTrue((dest / "superpersona").is_symlink())
            self.assertFalse((dest / "superadhd").exists())
