#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from github_im.content.catalog import build_module
from github_im.docx_builder import build_docx
from github_im.release_qa import audit_docx, audit_pdf
from github_im.validation import validate_module
from github_im.visuals import validate_visual_assets


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = ROOT / "GitHub_Fundamentals_CMU_Module.docx"
DEFAULT_PDF = ROOT / "GitHub_Fundamentals_CMU_Module.pdf"
ASSET_DIR = ROOT / "figures" / "cmu-module"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the CMU-format GitHub Fundamentals module.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    module = build_module()
    errors = validate_module(module) + validate_visual_assets(ASSET_DIR)
    if args.validate_only:
        errors += audit_docx(DEFAULT_OUTPUT)
        errors += audit_pdf(DEFAULT_PDF)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    if args.validate_only:
        print("Validation passed: content, visual assets, DOCX, and PDF contain no release errors.")
        return 0
    output = build_docx(module, ASSET_DIR, args.output)
    print(f"Created {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
