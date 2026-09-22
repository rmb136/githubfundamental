from pathlib import Path
import json
import tempfile
import unittest

from PIL import Image

from github_im import visuals
from github_im.content.catalog import build_module
from github_im.visuals import VISUALS, validate_visual_assets, write_manifest


class VisualAssetTests(unittest.TestCase):
    def test_catalog_maps_every_unit_to_one_visual(self):
        module = build_module()
        self.assertEqual(len(VISUALS), 13)
        self.assertEqual(
            {unit.figure_key for unit in module.units},
            set(VISUALS),
        )
        self.assertEqual(len({spec.filename for spec in VISUALS.values()}), 13)

    def test_final_visual_assets_are_print_ready(self):
        errors = validate_visual_assets(Path("figures/cmu-module"))
        self.assertEqual(errors, [])
        for spec in VISUALS.values():
            with Image.open(Path("figures/cmu-module") / spec.filename) as image:
                self.assertGreaterEqual(image.width, 1400)
                self.assertGreaterEqual(image.height, 800)
                self.assertGreaterEqual(image.width / image.height, 1.4)
                self.assertLessEqual(image.width / image.height, 2.0)

    def test_cover_visual_is_portrait_print_ready_and_prompted(self):
        self.assertTrue(hasattr(visuals, "COVER_VISUAL"))
        COVER_VISUAL = visuals.COVER_VISUAL
        self.assertEqual(COVER_VISUAL.filename, "cover-background.png")
        self.assertIn("stylized-concept", COVER_VISUAL.prompt)
        with Image.open(Path("figures/cmu-module") / COVER_VISUAL.filename) as image:
            self.assertGreaterEqual(image.width, 1000)
            self.assertGreaterEqual(image.height, 1400)
            self.assertGreater(image.height, image.width)

    def test_manifest_records_accessibility_and_prompts(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "visual_manifest.json"
            write_manifest(path)
            data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(len(data), 14)
        self.assertEqual(data[0]["key"], "cover-background")
        for item in data:
            self.assertTrue(item["caption"])
            self.assertTrue(item["alt_text"])
            self.assertTrue(item["prompt"])


if __name__ == "__main__":
    unittest.main()
