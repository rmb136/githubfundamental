from __future__ import annotations

from github_im.model import Module
from github_im.validation import validate_module

from .back_matter import build_back_matter
from .collaboration import build_collaboration_units
from .foundations import build_foundation_units
from .front_matter import build_front_matter
from .publishing import build_publishing_units


def build_module() -> Module:
    front = build_front_matter()
    back = build_back_matter()
    units = sorted(
        build_foundation_units() + build_collaboration_units() + build_publishing_units(),
        key=lambda unit: unit.number,
    )
    module = Module(
        title="GitHub Fundamentals for Beginner BSIT Students",
        audience="BSIT students with no prior Git experience",
        preface=front["preface"],
        glossary=front["glossary"],
        semester_roadmap=front["semester_roadmap"],
        units=units,
        capstone=back["capstone"],
        rubrics=back["rubrics"],
        references=back["references"],
    )
    errors = validate_module(module)
    if errors:
        raise ValueError("Invalid module:\n" + "\n".join(errors))
    return module
