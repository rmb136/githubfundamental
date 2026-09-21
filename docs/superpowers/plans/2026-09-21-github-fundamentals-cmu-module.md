# GitHub Fundamentals CMU Module Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a publication-ready, reproducible thirteen-unit GitHub Fundamentals module for beginner BSIT students in CMU format, including original instructional images, aligned assessments, an editable DOCX, and a matching PDF.

**Architecture:** Replace the single monolithic generator with a small `github_im` package: typed content models, three focused unit-content modules, a visual catalog, a DOCX builder, and automated quality checks. The existing top-level generator remains the stable entry point and orchestrates content validation, document generation, and final reporting. Thirteen generated raster illustrations live in `figures/cmu-module` and are inserted by stable asset keys so the final document remains reproducible.

**Tech Stack:** Bundled Python 3, `python-docx`, Pillow, standard-library `dataclasses`, `pytest`, OOXML helpers, built-in image generation, bundled Poppler, and the packaged document renderer or an available non-destructive office converter.

**Spec:** `docs/superpowers/specs/2026-09-21-github-fundamentals-cmu-module-design.md`

## Global Constraints

- Audience: BSIT students with no previous Git experience.
- Scope: thirteen sequential semester units using the topic order in the approved specification.
- Page format: A4 portrait, Arial 11-point body text, single line spacing, 1-inch top/bottom/right margins, and a 1.5-inch left margin.
- Required unit sequence: overview, rationale, behavioral objectives, instructions, pre-test, learning activities, concepts and discussion, self-test, post-test, supplementary reading, and APA references.
- Every objective must map to at least one activity and one assessment item.
- Use a consistent fictional `student-portfolio` repository throughout the module.
- Prefer `git switch` and `git restore`; mention `checkout` only as a common legacy equivalent.
- Never include real tokens, passwords, SSH private keys, personal data, or destructive commands without explicit safety guidance.
- Technical claims must be checked against current official Git documentation at `https://git-scm.com/docs` and GitHub Docs at `https://docs.github.com/`.
- Preserve all existing workspace files; write stable new deliverables named `GitHub_Fundamentals_CMU_Module.docx` and `GitHub_Fundamentals_CMU_Module.pdf`.
- Use the bundled Python runtime at `C:\Users\User-Pc\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`.
- Do not install packages or modify the user's system applications.
- The workspace is not currently a Git repository. Do not initialize one without user authorization; replace commit steps with a concise change checkpoint when `git rev-parse --is-inside-work-tree` fails.

## Review Focus

- **Incomplete unit data:** validation must reject any unit missing a required section, objective/activity/assessment alignment, answer, time allotment, or source.
- **Unsafe examples:** tests must reject embedded secrets and flag `git reset --hard`, unqualified force-push, or credential-like strings outside explicitly marked safety notes.
- **Broken visual assets:** validation must fail when an asset is missing, unreadable, too small for print, or mapped to the wrong unit.
- **CMU formatting drift:** structural tests must verify A4 dimensions, exact margins, Arial 11 body text, single spacing, and the required heading ladder.
- **Delivery mismatch:** final checks must require both DOCX and PDF, compare nonzero page counts, and scan extracted text for draft-marker phrases or missing unit headings.

---

### Task 1: Create the Content Model and Validation Foundation

**Files:**
- Create: `github_im/__init__.py`
- Create: `github_im/model.py`
- Create: `github_im/validation.py`
- Create: `tests/test_model_validation.py`

**Interfaces:**
- Produces: `Question`, `Activity`, `Unit`, `Module`, `validate_unit(unit: Unit) -> list[str]`, and `validate_module(module: Module) -> list[str]`.
- Consumes: no project-local interfaces.

- [ ] **Step 1: Write failing model-validation tests**

Create `tests/test_model_validation.py` with tests that instantiate one complete unit and assert that validation returns no errors. Add separate tests that remove `objectives`, `pretest`, `activities`, `self_test`, `posttest`, `references`, and `answer_key` and assert that the error identifies the exact missing field. Add these safety and alignment tests:

```python
def test_rejects_unmapped_objective(sample_unit):
    sample_unit.objectives.append("Configure a remote safely")
    assert "objective 4 has no activity mapping" in validate_unit(sample_unit)


def test_rejects_generic_answer(sample_unit):
    sample_unit.answer_key["post-1"] = "See the unit content."
    assert "post-1 uses a generic answer" in validate_unit(sample_unit)


def test_rejects_unqualified_destructive_command(sample_unit):
    sample_unit.discussion.append("Run git reset --hard HEAD~1.")
    assert "unsafe command lacks a safety note" in validate_unit(sample_unit)


def test_requires_thirteen_unique_units(complete_module):
    complete_module.units = complete_module.units[:12]
    assert "module must contain units 1 through 13 exactly once" in validate_module(complete_module)
```

- [ ] **Step 2: Run the tests and confirm failure**

Run:

```powershell
& 'C:\Users\User-Pc\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m pytest tests\test_model_validation.py -v
```

Expected: failure because `github_im.model` and `github_im.validation` do not exist.

- [ ] **Step 3: Implement typed content objects**

Create immutable identifiers and mutable content collections with these signatures:

```python
@dataclass
class Question:
    id: str
    prompt: str
    kind: Literal["multiple_choice", "short_answer", "performance"]
    answer: str
    choices: tuple[str, ...] = ()
    objective_ids: tuple[str, ...] = ()


@dataclass
class Activity:
    id: str
    title: str
    instructions: list[str]
    evidence: str
    objective_ids: tuple[str, ...]
    safety_note: str = ""


@dataclass
class Unit:
    number: int
    title: str
    time_allotment: str
    overview: str
    rationale: str
    objectives: list[str]
    objective_ids: list[str]
    learner_instructions: list[str]
    materials: list[str]
    pretest: list[Question]
    discussion: list[str]
    command_examples: list[tuple[str, str]]
    activities: list[Activity]
    self_test: list[Question]
    performance_task: Activity
    posttest: list[Question]
    supplementary_readings: list[str]
    references: list[str]
    figure_key: str
    answer_key: dict[str, str]


@dataclass
class Module:
    title: str
    audience: str
    preface: list[str]
    glossary: dict[str, str]
    semester_roadmap: list[dict[str, str]]
    units: list[Unit]
    capstone: Activity
    rubrics: dict[str, list[tuple[str, str]]]
    references: list[str]
```

- [ ] **Step 4: Implement validation**

`validate_unit` must enforce nonempty required fields, unique question IDs, five pre-test questions, at least five self-test questions, ten post-test questions, at least one activity, all objective IDs represented by an activity and assessment, specific answers for every question, and a nonempty figure key. `validate_module` must enforce units 1–13 exactly once, unique figure keys, a nonempty glossary, roadmap entries for all units, a capstone, and rubrics. Scan content case-insensitively for common draft markers, generic answer redirects, credential prompts, private-key headers, and unsafe commands lacking a nearby safety note.

- [ ] **Step 5: Run validation tests**

Run the Task 1 test command. Expected: all tests pass.

- [ ] **Step 6: Record the Task 1 checkpoint**

Run `git rev-parse --is-inside-work-tree`. If it succeeds, stage the four Task 1 files and commit with `feat: add CMU module content model`. If it fails, record the files and passing test command in the running implementation notes.

### Task 2: Author Front Matter and Units 1 Through 4

**Files:**
- Create: `github_im/content/__init__.py`
- Create: `github_im/content/front_matter.py`
- Create: `github_im/content/foundations.py`
- Create: `tests/test_foundation_content.py`

**Interfaces:**
- Consumes: `Question`, `Activity`, `Unit`, and `Module` types from Task 1.
- Produces: `build_front_matter() -> dict[str, object]` and `build_foundation_units() -> list[Unit]` containing units 1–4.

- [ ] **Step 1: Write failing content-contract tests**

Test the exact titles, objective counts, assessment counts, and practical outputs:

```python
EXPECTED = {
    1: ("Introduction to Git and GitHub", "concept-map.png"),
    2: ("Setting Up Git and GitHub", "configured Git identity and verified authentication"),
    3: ("Creating the First Repository", "student-portfolio repository with an initial commit"),
    4: ("Essential Git Commands", "three-commit history with a clean working tree"),
}


def test_foundation_unit_contracts():
    units = build_foundation_units()
    assert [unit.number for unit in units] == [1, 2, 3, 4]
    for unit in units:
        assert unit.title == EXPECTED[unit.number][0]
        assert 3 <= len(unit.objectives) <= 5
        assert len(unit.pretest) == 5
        assert len(unit.self_test) >= 5
        assert len(unit.posttest) == 10
        assert not validate_unit(unit)
```

Add assertions that Unit 2 discusses HTTPS and SSH without exposing credentials, Unit 3 includes `git init`, `git clone`, `git remote -v`, and `git push -u origin main`, and Unit 4 distinguishes working tree, index, and repository.

- [ ] **Step 2: Run the tests and confirm failure**

Run `python -m pytest tests\test_foundation_content.py -v` with the bundled Python. Expected: import failure.

- [ ] **Step 3: Author the front matter**

`front_matter.py` must provide a two-paragraph preface, at least 30 beginner glossary terms, and a thirteen-row semester roadmap. Each roadmap row contains `unit`, `title`, `time`, `output`, and `assessment`. Use two to three hours per unit, with additional independent practice for Units 5, 6, 9, 10, and 13.

- [ ] **Step 4: Author Unit 1**

Objectives must cover distinguishing Git from GitHub, identifying repository components, tracing a change from working directory to remote, and explaining the value of version history. The guided activity creates a paper or digital concept map. Discussion covers distributed version control, repository, commit, branch, remote, clone, and the four-stage mental model. The performance task is an accurate annotated concept map.

- [ ] **Step 5: Author Unit 2**

Objectives must cover installing and verifying Git, configuring name and email, selecting HTTPS or SSH appropriately, and confirming authentication without revealing secrets. Use `git --version`, `git config --global user.name`, `git config --global user.email`, `git config --global --list`, and safe verification steps. Include a safety note that private SSH keys and personal access tokens are never submitted as evidence.

- [ ] **Step 6: Author Unit 3**

Teach both create-on-GitHub-and-clone and initialize-locally-and-push paths, but designate the first as the beginner default. Use a public or private `student-portfolio` repository based on instructor direction. Include README creation, `git remote -v`, initial commit, and first push. The performance evidence is repository URL or instructor-approved screenshot plus the output of `git log --oneline` with personal information removed.

- [ ] **Step 7: Author Unit 4**

Teach `status`, `add`, `commit`, `log`, `diff`, `push`, `fetch`, and `pull` in a repeated edit-inspect-stage-commit-sync cycle. Include command/output examples that clearly separate unstaged, staged, committed, and remote states. The performance task requires three focused commits and a clean `git status`.

- [ ] **Step 8: Run Task 1 and Task 2 tests**

Run `python -m pytest tests\test_model_validation.py tests\test_foundation_content.py -v`. Expected: all tests pass.

- [ ] **Step 9: Record the Task 2 checkpoint**

Commit `github_im/content` and `tests/test_foundation_content.py` as `feat: add Git and repository foundation units` when Git is available; otherwise record the passing test command and changed files.

### Task 3: Author Units 5 Through 9

**Files:**
- Create: `github_im/content/collaboration.py`
- Create: `tests/test_collaboration_content.py`

**Interfaces:**
- Consumes: Task 1 models and validation.
- Produces: `build_collaboration_units() -> list[Unit]` containing units 5–9.

- [ ] **Step 1: Write failing tests for Units 5–9**

Assert exact titles, unit numbers, question counts, successful validation, and these required concepts:

```python
REQUIRED_COMMANDS = {
    5: {"git switch -c feature/about-page", "git merge feature/about-page"},
    6: {"git fetch origin", "git push -u origin feature/about-page"},
    7: set(),
    8: {"git check-ignore -v .env", "git log --oneline --graph --decorate --all"},
    9: set(),
}
```

Also assert that Unit 5 has a conflict-resolution activity, Unit 6 requires a reviewed pull request, Unit 7 requires a labeled issue and project-board movement, Unit 8 rejects committing `.env`, and Unit 9 contains a syntactically complete workflow stored under `.github/workflows`.

- [ ] **Step 2: Run the tests and confirm failure**

Run the Task 3 test file. Expected: import failure.

- [ ] **Step 3: Author Unit 5**

Teach branch purpose, `git switch -c`, branch naming, fast-forward versus three-way merge at a beginner level, merge conflicts, conflict markers, resolution, and branch cleanup. The guided activity creates two branches that edit the same controlled text file, resolves the conflict, runs `git status`, stages the resolution, and completes the merge. Explain that students must not resolve a conflict by blindly deleting all markers and content.

- [ ] **Step 4: Author Unit 6**

Teach collaborator and fork workflows, branch push, pull-request anatomy, review comments, requested changes, approvals, checks, and merge choices. The practical output is a pull request reviewed by a peer using a rubric covering title, rationale, focused diff, evidence of testing, and respectful response to feedback.

- [ ] **Step 5: Author Unit 7**

Teach actionable issue titles, problem statements, acceptance criteria, labels, assignees, milestones, issue-closing keywords, and GitHub Projects status movement. The performance task creates one well-scoped issue, links it to a project, moves it through two statuses, and closes it with evidence.

- [ ] **Step 6: Author Unit 8**

Teach README structure, `.gitignore`, small commits, meaningful messages, branch protection concepts, pull-before-push coordination, and when not to rewrite shared history. Include `.env`, build artifacts, editor files, and OS files in the ignore examples. Explicitly state that removing a secret from the latest commit does not remove it from history and requires credential revocation.

- [ ] **Step 7: Author Unit 9**

Teach events, workflows, jobs, runners, steps, actions, logs, and status checks. Use a complete beginner workflow in `.github/workflows/validate.yml` with `on: [push, pull_request]`, least-privilege `permissions: contents: read`, `actions/checkout` pinned to the current documented major release, and a shell step that verifies expected project files without requiring a language-specific toolchain. Explain secrets context without including secret values.

- [ ] **Step 8: Run validation and content tests**

Run all tests from Tasks 1–3. Expected: all pass.

- [ ] **Step 9: Record the Task 3 checkpoint**

Commit as `feat: add collaboration and automation units` when Git is available; otherwise record the passing tests and files.

### Task 4: Author Units 10 Through 13 and Instructor Back Matter

**Files:**
- Create: `github_im/content/publishing.py`
- Create: `github_im/content/back_matter.py`
- Create: `github_im/content/catalog.py`
- Create: `tests/test_advanced_content.py`
- Create: `tests/test_complete_module.py`

**Interfaces:**
- Consumes: `build_front_matter`, `build_foundation_units`, and `build_collaboration_units`.
- Produces: `build_publishing_units() -> list[Unit]`, `build_back_matter() -> dict[str, object]`, and `build_module() -> Module`.

- [ ] **Step 1: Write failing tests**

Assert Units 10–13 validate and the complete catalog returns exactly thirteen unique units. Require the capstone to map to Units 2–10 and require rubrics named `unit_performance`, `pull_request`, and `capstone`. Add assertions that the consolidated answer key contains every pre-test, self-test, and post-test ID.

- [ ] **Step 2: Run the tests and confirm failure**

Run the Task 4 tests. Expected: import failure.

- [ ] **Step 3: Author Unit 10**

Teach static-site constraints, a minimal `index.html`, repository and branch publishing sources, Pages settings, deployment status, and relative paths. The practical task publishes the `student-portfolio` site and verifies its public URL. Include privacy guidance: do not publish student IDs, home addresses, private contact details, or secrets.

- [ ] **Step 4: Author Unit 11**

Teach least privilege, two-factor authentication, collaborators and roles, secret scanning concepts, Dependabot alerts, code scanning, releases, tags, Packages, Insights, and API use cases at survey depth. The performance task audits a sample repository using a checklist and recommends three prioritized improvements. Do not require paid or organization-only features.

- [ ] **Step 5: Author Unit 12**

Teach repository discovery, README and contribution-guide review, code of conduct, license awareness, issue selection, fork-sync-branch workflow, focused commits, PR description, review response, and community etiquette. The practical task prepares a contribution plan or documentation-only pull request in an instructor-approved repository.

- [ ] **Step 6: Author Unit 13**

Teach diagnosis before repair using `status`, `log`, `diff`, `remote -v`, and `reflog`. Cover rejected pushes, authentication failure, detached HEAD, merge conflicts, accidental staging, amended commits, `git revert`, `git restore`, and recovery from reflog. Put `git reset --hard` and force-push in a clearly marked instructor-led recovery section with prerequisites, consequences, safer alternatives, and backup steps.

- [ ] **Step 7: Build the capstone, rubrics, cheat sheet, and answer key**

The capstone is a `student-portfolio` repository containing a README, static page, issue board, feature branch, pull request, reviewer feedback, merged change, validation workflow, and GitHub Pages deployment. The capstone rubric uses four levels across correctness, Git history, collaboration, documentation, automation, publication, security, and reflection. Unit rubrics use four levels across correctness, process, evidence, and safe practice. Generate answer-key entries directly from each `Question.answer` and include performance-task observable criteria.

- [ ] **Step 8: Assemble and validate the complete module**

`build_module()` must combine front matter, units sorted by number, and back matter, call `validate_module`, and raise `ValueError("Invalid module:\n" + "\n".join(errors))` on failure.

- [ ] **Step 9: Run all content tests**

Run `python -m pytest tests\test_model_validation.py tests\test_foundation_content.py tests\test_collaboration_content.py tests\test_advanced_content.py tests\test_complete_module.py -v`. Expected: all pass.

- [ ] **Step 10: Record the Task 4 checkpoint**

Commit as `feat: complete semester module content and assessments` when Git is available; otherwise record the content checkpoint.

### Task 5: Generate and Validate the Instructional Image Set

**Files:**
- Create: `github_im/visuals.py`
- Create: `figures/cmu-module/visual_manifest.json`
- Create: `figures/cmu-module/unit-01-version-control-flow.png`
- Create: `figures/cmu-module/unit-02-setup-authentication.png`
- Create: `figures/cmu-module/unit-03-repository-lifecycle.png`
- Create: `figures/cmu-module/unit-04-command-flow.png`
- Create: `figures/cmu-module/unit-05-branch-merge.png`
- Create: `figures/cmu-module/unit-06-pull-request-cycle.png`
- Create: `figures/cmu-module/unit-07-issues-projects.png`
- Create: `figures/cmu-module/unit-08-healthy-repository.png`
- Create: `figures/cmu-module/unit-09-actions-pipeline.png`
- Create: `figures/cmu-module/unit-10-pages-publishing.png`
- Create: `figures/cmu-module/unit-11-security-layers.png`
- Create: `figures/cmu-module/unit-12-open-source-contribution.png`
- Create: `figures/cmu-module/unit-13-troubleshooting-path.png`
- Create: `tests/test_visual_assets.py`

**Interfaces:**
- Consumes: each `Unit.figure_key`.
- Produces: `VISUALS: dict[str, VisualSpec]`, `validate_visual_assets(base_dir: Path) -> list[str]`, and thirteen print-ready PNGs.

- [ ] **Step 1: Write failing visual tests**

Test that all thirteen `figure_key` values map to unique `VisualSpec` records; every asset exists; Pillow can open it; width is at least 1400 pixels; height is at least 800 pixels; aspect ratio is between 1.4 and 2.0; the manifest contains nonempty `caption`, `alt_text`, `prompt`, and `unit`; and no image filename contains spaces.

- [ ] **Step 2: Implement `VisualSpec` and validation**

Use:

```python
@dataclass(frozen=True)
class VisualSpec:
    key: str
    unit: int
    filename: str
    caption: str
    alt_text: str
    prompt: str
```

`validate_visual_assets` must report missing files, unreadable images, small dimensions, wrong aspect ratio, duplicate files, empty accessibility text, and mismatch between manifest unit numbers and `VISUALS`.

- [ ] **Step 3: Define thirteen exact prompts in the manifest**

Every prompt uses `Use case: scientific-educational`, `Asset type: printed university instructional module figure`, `Style/medium: clean flat educational illustration with crisp vector-like forms`, `Color palette: deep blue, medium blue, pale blue, charcoal, white`, `Composition/framing: landscape, generous margins, clear left-to-right or top-to-bottom sequence`, and `Constraints: no logos, no watermark, no photorealism, no decorative characters, no tiny interface text, no unsupported commands`.

The primary requests are:

1. Four connected zones showing a student file moving from working directory to staging area to local repository to cloud remote, with visually distinct states and reversible arrows for fetch and pull.
2. A beginner workstation setup journey showing Git installation, identity configuration, and a safe choice between HTTPS and SSH authentication, with a shield representing credential safety.
3. Two accurate repository-start paths converging on first push: create remote then clone, and initialize local then add remote; use objects and arrows, not dense text.
4. A clear edit-inspect-stage-commit-sync cycle showing file changes, status inspection, staging, local history, and remote synchronization.
5. A main branch and feature branch diverging, receiving separate commits, merging, and resolving one controlled conflict without data loss.
6. A collaborative pull-request cycle showing issue selection, branch or fork, focused commits, push, pull request, peer review, revision, checks, and merge.
7. An issue moving through backlog, in progress, review, and done while labels, assignee, milestone, and linked pull request remain visibly connected.
8. A healthy repository ecosystem showing README, ignore rules, small commits, protected main branch, review, automated checks, and no exposed secrets.
9. A continuous-integration pipeline showing push or pull-request trigger, workflow file, hosted runner, checkout, validation steps, and pass or fail result.
10. A static-site publishing flow showing repository files, selected publishing source, build or deployment process, and a public website viewed in a browser.
11. Concentric repository security layers showing account protection, least-privilege access, secret protection, dependency review, code scanning, and monitored alerts.
12. An open-source contribution journey showing project discovery, reading community files, choosing an issue, fork and branch, focused change, pull request, respectful review, and accepted contribution.
13. A beginner troubleshooting decision path beginning with observe status and error, then branching to authentication, synchronization, conflict, detached-head, and recovery outcomes using safe-first choices.

- [ ] **Step 4: Generate the image assets**

Use the built-in image-generation tool once per `VisualSpec`; do not use the CLI fallback. Request landscape output with no embedded prose. Inspect each result, copy the accepted output into `figures/cmu-module` using the stable filename, and record the final prompt in `visual_manifest.json`.

- [ ] **Step 5: Inspect every image**

Open each workspace PNG with the local image viewer at original detail. Reject and regenerate any image with malformed symbols, misleading arrow direction, pseudo-text that resembles commands, inconsistent palette, poor print contrast, or irrelevant decoration. Confirm each accepted image matches its caption and alt text.

- [ ] **Step 6: Run visual tests**

Run `python -m pytest tests\test_visual_assets.py -v`. Expected: all pass.

- [ ] **Step 7: Record the Task 5 checkpoint**

Commit the catalog, manifest, tests, and accepted images as `feat: add instructional workflow illustrations` when Git is available; otherwise record all final asset paths and prompts in the checkpoint.

### Task 6: Build the CMU-Compliant DOCX Generator

**Files:**
- Create: `github_im/docx_builder.py`
- Create: `github_im/ooxml.py`
- Modify: `generate_github_fundamentals_docx.py`
- Create: `tests/test_docx_builder.py`

**Interfaces:**
- Consumes: `build_module() -> Module` and `VISUALS`.
- Produces: `build_docx(module: Module, asset_dir: Path, output_path: Path) -> Path` and CLI output `GitHub_Fundamentals_CMU_Module.docx`.

- [ ] **Step 1: Write failing DOCX structural tests**

Build a temporary document and assert:

```python
assert section.page_width == Mm(210)
assert section.page_height == Mm(297)
assert section.top_margin == Inches(1)
assert section.bottom_margin == Inches(1)
assert section.left_margin == Inches(1.5)
assert section.right_margin == Inches(1)
assert document.styles["Normal"].font.name == "Arial"
assert document.styles["Normal"].font.size == Pt(11)
assert document.styles["Normal"].paragraph_format.line_spacing == 1
```

Also assert that the document contains Title, Preface, Table of Contents, Glossary, Semester Roadmap, all Unit 1–13 headings, Capstone Project, Assessment Rubrics, Answer Key, Command Cheat Sheet, References, and About the Author. Assert exactly thirteen unit figures, captions beginning `Figure 1` through `Figure 13`, and nonempty image descriptions in the drawing XML.

- [ ] **Step 2: Run the tests and confirm failure**

Run `python -m pytest tests\test_docx_builder.py -v`. Expected: import failure.

- [ ] **Step 3: Implement styles and page geometry**

Create black Title, Heading 1, Heading 2, and Heading 3 styles with Arial and controlled spacing. Use Arial 11, single spacing, 6 points after body paragraphs, widow/orphan control, and keep-with-next for headings. Create `Command` style with Consolas 9.5, pale-gray paragraph shading, left/right indentation, and no fixed-height containers. Use light-gray borders, dark-blue headers, alternating pale-blue rows, deliberate cell padding, vertically centered cells, and repeating table headers.

- [ ] **Step 4: Implement OOXML helpers**

Provide helpers for PAGE fields, a TOC field, bookmarks, image description attributes, repeated table headers, cell shading, cell margins, and light-gray borders. Each helper must accept and return the exact `python-docx` object it modifies so tests can inspect results.

- [ ] **Step 5: Implement front matter and roadmap rendering**

Use Word's Title style for `GitHub Fundamentals for Beginner BSIT Students`. Add the subtitle `A CMU Format Instructional Module`, neutral edition information, and no invented author credentials. Render the preface, real TOC field, list of figures, glossary, and a five-column roadmap table. Start the main module after a page break.

- [ ] **Step 6: Implement unit rendering**

For each unit, render the number/title, time allotment, overview, rationale, objectives, learner instructions, materials, five-item pre-test, figure, concept discussion, command examples, activities, self-test, performance task, ten-item post-test, readings, and APA references. Use automatic numbered lists and keep figure/caption pairs together. Put answer keys only in the instructor back matter so students do not see answers adjacent to questions.

- [ ] **Step 7: Implement back matter rendering**

Render the capstone, rubrics, consolidated answer key, command cheat sheet, consolidated references, and About the Author. The About the Author page must state that author details are supplied by the author before publication and must not invent a name, degree, rank, or affiliation.

- [ ] **Step 8: Replace the top-level generator**

The CLI must accept `--output`, `--asset-dir`, and `--validate-only`; default to the stable DOCX filename and `figures/cmu-module`; call `build_module`; validate content and images; build the DOCX; and exit nonzero with concise messages on failure. Remove dependency auto-installation, timestamped output, generic image creation, and incomplete text answer-key generation.

- [ ] **Step 9: Mark the DOCX edit operation and run the generator**

Immediately before the first successful authoring run, execute the document-skill marker exactly once with operation kind `edit`, expected output count `1`, and output format `docx`, using the bundled Node executable and the marker script from the document skill package. Then run the generator with the bundled Python.

- [ ] **Step 10: Run DOCX tests**

Run all existing tests plus `tests\test_docx_builder.py`. Expected: all pass and a nonempty `GitHub_Fundamentals_CMU_Module.docx` exists.

- [ ] **Step 11: Record the Task 6 checkpoint**

Commit generator, package files, tests, and the DOCX as `feat: generate CMU formatted GitHub module` when Git is available; otherwise record the passing commands and output path.

### Task 7: Render, Inspect, and Produce the Matching PDF

**Files:**
- Create: `github_im/release_qa.py`
- Create: `tests/test_release_qa.py`
- Create: `.tmp/final-render/` as disposable QA output.
- Create: `GitHub_Fundamentals_CMU_Module.pdf`

**Interfaces:**
- Consumes: final DOCX and structured module catalog.
- Produces: `audit_docx(path: Path) -> list[str]`, `audit_pdf(path: Path, expected_units: int = 13) -> list[str]`, final page PNGs for internal inspection, and final PDF.

- [ ] **Step 1: Write failing release-audit tests**

Test that audits reject missing/empty files, Letter page geometry, missing unit headings, missing figure captions, draft-marker phrases, incomplete answer keys, and PDF text lacking any Unit 1–13 heading. Add a test that a PDF with zero pages fails and a test that extracted text containing a private-key header fails.

- [ ] **Step 2: Implement structural release audits**

Use `python-docx`, `zipfile`, and `pypdf` or `pdfplumber` from the bundled runtime. `audit_docx` checks page geometry, styles, headings, relationships, captions, image descriptions, required front/back matter, and draft-marker scans. `audit_pdf` checks nonzero pages, unit headings, captions, front/back matter, and forbidden text. Return deterministic error strings.

- [ ] **Step 3: Render the final DOCX**

Use the packaged `render_docx.py` with the bundled Python. If the packaged runtime cannot locate an office converter, locate an available converter without installing or modifying software. If using Microsoft Word automation or another external desktop converter requires permission, request approval before running it. Generate page PNGs and an emitted PDF under `.tmp/final-render`.

- [ ] **Step 4: Inspect every rendered page**

Open every PNG at original detail. Check title/front matter, all thirteen unit openings, every table continuation, every image/caption pair, command examples, answer keys, rubrics, references, page numbers, and final author page. Record page-specific defects, correct the builder/content, rebuild, and repeat the full render until no defects remain.

- [ ] **Step 5: Mark the PDF edit operation and create the stable PDF**

Immediately before authoring the final PDF, execute the PDF-skill marker exactly once with operation kind `edit`, expected output count `1`, and output format `pdf`. Copy the verified emitted PDF to `GitHub_Fundamentals_CMU_Module.pdf` only after the rendered pages pass inspection.

- [ ] **Step 6: Run release audits and the full test suite**

Run:

```powershell
& 'C:\Users\User-Pc\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m pytest tests -v
& 'C:\Users\User-Pc\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' generate_github_fundamentals_docx.py --validate-only
```

Expected: all tests pass and validation reports zero content, visual, DOCX, and PDF errors.

- [ ] **Step 7: Record the Task 7 checkpoint**

Commit release QA, tests, and final PDF as `test: verify CMU module release artifacts` when Git is available; otherwise record the full passing test output, DOCX page count, PDF page count, and final file sizes.

### Task 8: Final Specification Audit and Delivery

**Files:**
- Verify: `docs/superpowers/specs/2026-09-21-github-fundamentals-cmu-module-design.md`
- Verify: `GitHub_Fundamentals_CMU_Module.docx`
- Verify: `GitHub_Fundamentals_CMU_Module.pdf`
- Verify: `figures/cmu-module/visual_manifest.json`

**Interfaces:**
- Consumes: every output from Tasks 1–7.
- Produces: the final user-facing delivery summary and artifact citations.

- [ ] **Step 1: Check specification coverage**

Create a temporary checklist mapping every success criterion, CMU format requirement, required section, learning-design rule, assessment rule, visual requirement, deliverable, and verification item to a file, test, or inspected page. Resolve every uncovered item before delivery.

- [ ] **Step 2: Search for prohibited residue**

Run case-insensitive searches across source, extracted DOCX text, PDF text, and manifest for common draft markers, generic answer redirects, old generated-question stems, credential prompts, private-key headers, and internal tool tokens. Expected: no instructional-content matches.

- [ ] **Step 3: Confirm preservation and stable outputs**

Verify that the original DOCX, PDF, timestamped files, forms, guidelines, and existing figures remain present and unchanged. Confirm the final DOCX, PDF, generator, package, tests, and thirteen selected visuals exist at their stable paths.

- [ ] **Step 4: Perform completion verification**

Run the full test suite and both release audits one final time after the last edit. Record exact command results; do not rely on results from an earlier build.

- [ ] **Step 5: Deliver only final artifacts**

Provide one output citation for the final DOCX and one output citation for the final PDF. Summarize CMU compliance, the thirteen-unit learning design, generated illustrations, aligned assessments, answer keys, and QA status. Do not link internal page renders or temporary files unless the user asks.
