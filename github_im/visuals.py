from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path

from PIL import Image


@dataclass(frozen=True)
class VisualSpec:
    key: str
    unit: int
    filename: str
    caption: str
    alt_text: str
    prompt: str


COVER_PROMPT = """Use case: stylized-concept
Asset type: premium portrait book-cover illustration for a university instructional module
Primary request: Create a sophisticated, modern visual metaphor for learning Git and GitHub fundamentals, showing a luminous branching pathway of connected commit nodes that begins as a single line, branches into several clean paths, and confidently converges toward a bright horizon. Include subtle abstract cues of code, folders, collaboration, and version history as elegant geometric forms, without resembling a software screenshot.
Scene/backdrop: deep navy-to-midnight-blue atmospheric field with layered translucent contours and gentle depth; a concentrated cyan and electric-blue glow through the central branching network; subtle warm gold highlights for academic prestige.
Style/medium: polished editorial technology illustration, refined 3D vector-like geometry with soft volumetric lighting, professional university textbook quality, elegant and uncluttered.
Composition/framing: portrait A4-friendly composition; central visual occupies the middle 60 percent; generous calm negative space near the top and bottom for separately typeset title and author; balanced, print-safe edges.
Lighting/mood: confident, aspirational, intellectually rigorous, welcoming to beginners.
Color palette: deep navy, cobalt blue, cyan, restrained gold, crisp white light.
Constraints: no text, no letters, no numbers, no logos, no brand marks, no mascots, no user interface, no watermark; ensure clear visual hierarchy and high contrast suitable for print."""

COVER_VISUAL = VisualSpec(
    key="cover-background",
    unit=0,
    filename="cover-background.png",
    caption="A branching path from first commit to confident collaboration",
    alt_text="Abstract Git learning journey with luminous commit nodes branching through code, file, collaboration, and history symbols toward a bright horizon.",
    prompt=COVER_PROMPT,
)


BASE_PROMPT = """Use case: scientific-educational
Asset type: printed university instructional module figure
Style/medium: clean flat educational illustration with crisp vector-like forms
Color palette: deep navy blue, medium blue, pale blue, charcoal, and white, with one amber accent only for warnings
Composition/framing: 16:9 landscape, generous outer margins, clear visual hierarchy and left-to-right or top-to-bottom sequence
Lighting/mood: bright, calm, precise, approachable for beginner computing students
Constraints: no logos, no watermark, no photorealism, no decorative characters, no tiny interface text, no source-code text, no unsupported commands, no random letters, no pseudo-words; use simple universally understood symbols and leave labeling to the document caption
"""


def _spec(unit, key, filename, caption, alt_text, primary_request):
    return VisualSpec(
        key=key,
        unit=unit,
        filename=filename,
        caption=caption,
        alt_text=alt_text,
        prompt=BASE_PROMPT + "Primary request: " + primary_request,
    )


_ITEMS = [
    _spec(1, "unit-01-version-control-flow", "unit-01-version-control-flow.png", "From a working file to shared repository history", "Four connected stages show a changed file moving through the working tree, staging area, local repository, and remote repository.", "Four connected zones showing a student file moving from a working folder to a selection tray to a local history archive to a cloud remote, with distinct states and reverse synchronization arrows."),
    _spec(2, "unit-02-setup-authentication", "unit-02-setup-authentication.png", "A secure Git and GitHub setup path", "A workstation setup path covers Git installation, identity configuration, and the choice between HTTPS and SSH authentication.", "A beginner workstation setup journey showing software installation, identity configuration, and a safe fork between HTTPS and SSH authentication, with a shield representing credential safety."),
    _spec(3, "unit-03-repository-lifecycle", "unit-03-repository-lifecycle.png", "Two paths to the first published repository", "Remote-first cloning and local-first initialization converge on the first repository push.", "Two accurate repository-start paths converging on first publication: create a remote then clone, or initialize a local project then connect a remote; use folder, archive, cloud, and arrow symbols only."),
    _spec(4, "unit-04-command-flow", "unit-04-command-flow.png", "The inspect stage commit and synchronize cycle", "A cyclical workflow shows editing, inspecting, staging, committing, and synchronizing a project.", "A clear recurring edit-inspect-select-record-synchronize cycle showing a changed document, status inspection, staging tray, local history, and remote synchronization."),
    _spec(5, "unit-05-branch-merge", "unit-05-branch-merge.png", "Feature branching merging and conflict resolution", "A main branch and feature branch diverge, receive commits, encounter a controlled conflict, and merge into verified history.", "A main line and feature line diverging from one commit, receiving separate changes, meeting at a controlled conflict junction, then merging into a verified shared line without data loss."),
    _spec(6, "unit-06-pull-request-cycle", "unit-06-pull-request-cycle.png", "The collaborative pull request cycle", "A circular workflow connects an issue, feature work, a pull request, peer review, revision, checks, and merge.", "A collaborative cycle showing task selection, focused branch work, published proposal, peer review conversation, revision, automated check, approval, and merge."),
    _spec(7, "unit-07-issues-projects", "unit-07-issues-projects.png", "Tracking work from backlog to completion", "One work item moves through backlog, active work, review, and done while ownership and milestone links remain visible.", "One work card moving across a four-column planning board from backlog through active work and review to completion, with small connected symbols for category, owner, milestone, and implementation."),
    _spec(8, "unit-08-healthy-repository", "unit-08-healthy-repository.png", "Elements of a healthy repository", "A repository is surrounded by documentation, ignore rules, focused commits, protected review, automated checks, and secret protection.", "A healthy central project repository surrounded by six connected safeguards: clear documentation, excluded sensitive files, small commit history, protected main line, peer review, and automated validation."),
    _spec(9, "unit-09-actions-pipeline", "unit-09-actions-pipeline.png", "A continuous integration validation pipeline", "A repository event starts a workflow that runs checkout and validation steps and ends in a clear pass or fail result.", "A left-to-right continuous-integration pipeline showing repository event, workflow document, hosted runner, source retrieval, validation steps, and a final pass-or-fail gate."),
    _spec(10, "unit-10-pages-publishing", "unit-10-pages-publishing.png", "Publishing a static site with GitHub Pages", "Repository web files pass through a publishing source and deployment process to become a public browser site.", "A static-site publishing path showing repository web files, selected source branch or folder, deployment process, and a polished public site in a browser frame."),
    _spec(11, "unit-11-security-layers", "unit-11-security-layers.png", "Layered protection for an account and repository", "Concentric protection layers represent account security, least privilege, secret safety, dependency review, code scanning, and alerts.", "Concentric repository security layers showing protected account, least-privilege access, secret shield, dependency review, code scanning, and monitored alert signals."),
    _spec(12, "unit-12-open-source-contribution", "unit-12-open-source-contribution.png", "An open source contribution journey", "A contributor moves from project discovery and community guidance through an issue, fork, focused change, pull request, review, and acceptance.", "An open-source contribution journey showing project discovery, reading community guidance, selecting a small issue, creating an independent copy and branch, focused improvement, proposal, respectful review, and accepted contribution."),
    _spec(13, "unit-13-troubleshooting-path", "unit-13-troubleshooting-path.png", "A safe first troubleshooting decision path", "A decision path starts with evidence collection and branches toward authentication, synchronization, conflict, detached-head, and recovery outcomes.", "A beginner troubleshooting decision tree beginning with observation and evidence, then branching to credential access, synchronization, conflict, detached work, and recovery, always favoring safe reversible paths before an amber expert-only warning path."),
]

VISUALS = {item.key: item for item in _ITEMS}


def validate_visual_assets(base_dir: Path) -> list[str]:
    errors: list[str] = []
    cover_path = base_dir / COVER_VISUAL.filename
    if not cover_path.exists():
        errors.append(f"{COVER_VISUAL.key}: missing asset {cover_path}")
    else:
        try:
            with Image.open(cover_path) as image:
                image.verify()
            with Image.open(cover_path) as image:
                cover_width, cover_height = image.size
        except Exception as exc:
            errors.append(f"{COVER_VISUAL.key}: unreadable image: {exc}")
        else:
            if cover_width < 1000 or cover_height < 1400:
                errors.append(f"{COVER_VISUAL.key}: image is too small ({cover_width}x{cover_height})")
            if cover_height <= cover_width:
                errors.append(f"{COVER_VISUAL.key}: cover image must use portrait orientation")
    seen_files: set[str] = set()
    for key, spec in VISUALS.items():
        if not spec.caption or not spec.alt_text or not spec.prompt:
            errors.append(f"{key}: caption, alt text, and prompt are required")
        if spec.filename in seen_files:
            errors.append(f"{key}: duplicate filename {spec.filename}")
        seen_files.add(spec.filename)
        if " " in spec.filename:
            errors.append(f"{key}: filename contains spaces")
        path = base_dir / spec.filename
        if not path.exists():
            errors.append(f"{key}: missing asset {path}")
            continue
        try:
            with Image.open(path) as image:
                image.verify()
            with Image.open(path) as image:
                width, height = image.size
        except Exception as exc:
            errors.append(f"{key}: unreadable image: {exc}")
            continue
        if width < 1400 or height < 800:
            errors.append(f"{key}: image is too small ({width}x{height})")
        ratio = width / height
        if not 1.4 <= ratio <= 2.0:
            errors.append(f"{key}: aspect ratio {ratio:.2f} is outside 1.4-2.0")
    return errors


def write_manifest(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps([asdict(COVER_VISUAL), *[asdict(item) for item in _ITEMS]], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return path
