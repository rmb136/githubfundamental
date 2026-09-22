from __future__ import annotations

from github_im.model import Activity

from .common import GITHUB_REFERENCE, GIT_REFERENCE


def build_back_matter() -> dict[str, object]:
    capstone = Activity(
        id="capstone",
        title="Capstone: Publish a Reviewed Student Portfolio",
        instructions=[
            "Verify Git identity and repository authentication without submitting any credential.",
            "Create or refine the student-portfolio repository with an accurate README and safe .gitignore.",
            "Create an issue with acceptance criteria and track it on a project view.",
            "Implement the issue on a focused feature branch with small, descriptive commits.",
            "Open a pull request, obtain peer review, address feedback, and merge after checks pass.",
            "Add a least-privilege validation workflow under .github/workflows.",
            "Publish the approved static portfolio through GitHub Pages and verify the public site.",
            "Submit a reflection connecting repository evidence to the Git and GitHub concepts learned.",
        ],
        evidence="Repository URL, issue, project evidence, feature branch history, reviewed pull request, passing workflow, GitHub Pages URL, and reflection",
        objective_ids=tuple(f"unit-{number}" for number in range(2, 11)),
        safety_note="Exclude credentials, private keys, tokens, private student data, grades, and unlicensed material from the repository and evidence.",
    )
    rubrics = {
        "unit_performance": [
            ("Correctness", "4: accurate and complete; 3: minor correction; 2: partial; 1: incorrect or missing"),
            ("Process", "4: deliberate safe workflow; 3: one avoidable step; 2: repeated guidance needed; 1: unsafe or undocumented"),
            ("Evidence", "4: sufficient and clearly labeled; 3: mostly sufficient; 2: incomplete; 1: absent"),
            ("Safe practice", "4: protects credentials and data; 3: minor privacy correction; 2: unsafe tendency corrected; 1: exposed or mishandled sensitive data"),
        ],
        "pull_request": [
            ("Scope", "4: one focused issue; 3: small unrelated change; 2: broad diff; 1: purpose unclear"),
            ("Description", "4: rationale, changes, evidence, and issue link; 3: one item weak; 2: several missing; 1: absent"),
            ("Review response", "4: respectful and evidence-based; 3: addressed with minor gaps; 2: incomplete; 1: ignored or inappropriate"),
            ("Checks", "4: all required checks pass; 3: nonblocking warning explained; 2: failure unresolved; 1: no validation"),
        ],
        "capstone": [
            ("Repository correctness", "4: complete and functional; 3: minor defect; 2: multiple gaps; 1: unusable"),
            ("Git history", "4: focused, readable commits; 3: mostly focused; 2: inconsistent; 1: missing or confusing"),
            ("Collaboration", "4: traceable issue, review, revision, merge; 3: one gap; 2: limited evidence; 1: absent"),
            ("Documentation", "4: accurate README and reflection; 3: minor omissions; 2: incomplete; 1: absent"),
            ("Automation", "4: useful least-privilege passing workflow; 3: works with minor issue; 2: unreliable; 1: absent"),
            ("Publication", "4: accessible verified Pages site; 3: minor defect; 2: unstable; 1: absent"),
            ("Security", "4: safe data and access practice; 3: minor correction; 2: material concern corrected; 1: exposed sensitive data"),
            ("Reflection", "4: evidence-based synthesis; 3: sound but general; 2: superficial; 1: absent"),
        ],
    }
    return {"capstone": capstone, "rubrics": rubrics, "references": [GIT_REFERENCE, GITHUB_REFERENCE]}
