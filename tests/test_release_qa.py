import tempfile
import unittest
from pathlib import Path

from docx import Document
from docx.shared import Inches
from pypdf import PdfWriter

from github_im.content.catalog import build_module
from github_im.docx_builder import build_docx
from github_im.release_qa import audit_docx, audit_pdf, audit_pdf_text


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "figures" / "cmu-module"


class ReleaseQATests(unittest.TestCase):
    def test_docx_accepts_cover_artwork_plus_thirteen_unit_figures(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "module.docx"
            build_docx(build_module(), ASSETS, path)
            errors = audit_docx(path)
        self.assertFalse(any("figures; expected" in error for error in errors), errors)

    def test_docx_rejects_missing_and_empty_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertIn("DOCX file is missing.", audit_docx(root / "missing.docx"))
            empty = root / "empty.docx"
            empty.write_bytes(b"")
            self.assertIn("DOCX file is empty.", audit_docx(empty))

    def test_docx_rejects_letter_geometry_and_missing_release_sections(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "letter.docx"
            document = Document()
            section = document.sections[0]
            section.page_width, section.page_height = Inches(8.5), Inches(11)
            document.add_paragraph("TODO draft")
            document.save(path)
            errors = audit_docx(path)
        self.assertIn("DOCX page size is not A4.", errors)
        self.assertTrue(any("missing required section" in error for error in errors))
        self.assertTrue(any("draft marker" in error for error in errors))
        self.assertTrue(any("answer key" in error.lower() for error in errors))

    def test_pdf_rejects_zero_pages(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "zero.pdf"
            writer = PdfWriter()
            with path.open("wb") as stream:
                writer.write(stream)
            self.assertIn("PDF contains zero pages.", audit_pdf(path))

    def test_pdf_text_rejects_missing_units_and_private_key(self):
        errors = audit_pdf_text("Preface\nBEGIN OPENSSH PRIVATE KEY", expected_units=13)
        self.assertTrue(any("Unit 13" in error for error in errors))
        self.assertIn("PDF contains forbidden secret material.", errors)


if __name__ == "__main__":
    unittest.main()
