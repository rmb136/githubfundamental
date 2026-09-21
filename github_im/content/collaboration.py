from __future__ import annotations

from .common import GITHUB_REFERENCE, GIT_REFERENCE, make_unit


def build_collaboration_units():
    return [_unit_5(), _unit_6(), _unit_7(), _unit_8(), _unit_9()]


def _unit_5():
    return make_unit(
        number=5,
        title="Branching and Merging",
        time_allotment="3 hours",
        overview="Students isolate work on a feature branch, inspect branch history, merge a completed change, and resolve a controlled conflict.",
        rationale="Branches let teams develop and review changes without destabilizing the shared default branch.",
        objectives=["Create and switch branches safely.", "Explain divergence and merge outcomes.", "Merge a focused feature into main.", "Resolve a text conflict without discarding valid work."],
        learner_instructions=["Begin with a clean working tree.", "Use the assigned feature branch name.", "Read conflict markers before editing."],
        materials=["student-portfolio repository", "Text editor", "Terminal"],
        discussion=[
            "A branch is a movable reference to the latest commit in a line of development. Creating a branch is inexpensive because Git stores commits once and moves names as new commits are added.",
            "`git switch -c` creates a branch from the current commit and checks it out. The working tree then reflects that branch, and new commits advance it rather than main.",
            "A fast-forward merge moves the target branch name forward when no competing commits exist. A three-way merge combines divergent histories and records a merge commit when necessary.",
            "A conflict occurs when Git cannot safely decide how competing edits should be combined. Conflict markers show the current and incoming content; they are instructions for a human decision, not content to commit.",
            "Conflict resolution means constructing the correct final file, removing all markers, testing or reviewing it, staging the resolved file, and completing the merge. Branch deletion happens only after the work is safely integrated.",
        ],
        command_examples=[
            ("git switch -c feature/about-page", "Creates and checks out a focused feature branch."),
            ("git branch --show-current", "Confirms the active branch before editing."),
            ("git log --oneline --graph --decorate --all", "Shows branch divergence and merge structure."),
            ("git switch main", "Returns to the target branch."),
            ("git merge feature/about-page", "Integrates the completed feature into main."),
            ("git branch -d feature/about-page", "Deletes the integrated local branch after verification."),
        ],
        activity_title="Develop and merge an About page",
        activity_steps=[
            "Create feature/about-page from an up-to-date main branch and add about.html.",
            "Commit the page on the feature branch and inspect the graph.",
            "Create a controlled conflicting edit in an instructor-provided practice file on both branches.",
            "Merge, inspect the conflict markers, preserve the intended content from both sides, and remove every marker.",
            "Stage the resolved file, complete the merge, inspect history, and delete the feature branch after verification.",
        ],
        evidence="A merged feature, resolved conflict file, and graph showing the integrated history",
        safety_note="Resolve conflicts only in the practice repository; make a backup before experimenting with history changes.",
        assessment_items=[
            ("What does a branch point to?", "A branch points to the latest commit in its line of development."),
            ("What does git switch -c do?", "It creates a new branch from the current commit and checks it out."),
            ("Why confirm the active branch before editing?", "It prevents committing work to the wrong line of development."),
            ("When is a merge fast-forward?", "When the target has no new divergent commits and can move directly to the source tip."),
            ("What causes a merge conflict?", "Competing changes that Git cannot safely combine automatically."),
            ("What do conflict markers represent?", "They delimit the current and incoming versions that require a human resolution."),
            ("What is the goal of conflict resolution?", "To produce the correct final file, not merely remove marker lines."),
            ("How is a resolved file recorded?", "Review it, stage it, and complete the merge commit when required."),
            ("When is local branch deletion safe?", "After its work is integrated and verified or otherwise preserved."),
            ("Why inspect the commit graph?", "It confirms branch relationships, divergence, and merge results."),
        ],
        supplementary_readings=["Git reference: git-switch", "Git reference: git-merge"],
        references=[GIT_REFERENCE],
        figure_key="unit-05-branch-merge",
    )


def _unit_6():
    return make_unit(
        number=6,
        title="Collaborating with Teams",
        time_allotment="3 hours",
        overview="Students use branches or forks, pull requests, review comments, automated checks, and merge decisions to collaborate transparently.",
        rationale="A pull request turns code integration into a reviewable conversation with evidence, ownership, and a durable decision record.",
        objectives=["Select a branch or fork workflow.", "Open a focused pull request.", "Review changes constructively.", "Revise and merge after requirements are met."],
        learner_instructions=["Use an instructor-assigned partner.", "Keep the pull request focused on one issue.", "Respond to review comments respectfully and with evidence."],
        materials=["Shared or forked repository", "GitHub account", "Review rubric"],
        discussion=[
            "Collaborators with write access commonly create branches in one repository. External contributors commonly fork, clone the fork, and open a pull request back to the original repository.",
            "A pull request identifies a source branch, target branch, purpose, related issue, and visible diff. A good description explains why the change is needed, what changed, and how it was checked.",
            "Reviewers examine correctness, scope, clarity, safety, and test evidence. Comments should identify a specific observation and desired outcome rather than judging the contributor.",
            "Requested changes are part of collaboration. New commits pushed to the source branch update the same pull request, preserving the discussion and review history.",
            "Merging should occur only after required reviews and checks pass. Merge, squash, and rebase strategies produce different histories; the repository's contribution policy determines which is appropriate.",
        ],
        command_examples=[
            ("git fetch origin", "Updates remote-tracking information before starting work."),
            ("git switch -c feature/about-page origin/main", "Creates a feature branch from current remote main."),
            ("git push -u origin feature/about-page", "Publishes the feature branch and sets its upstream."),
            ("git log origin/main..HEAD --oneline", "Lists commits proposed by the current branch."),
            ("git diff origin/main...HEAD", "Reviews the complete proposed change before opening a pull request."),
        ],
        activity_title="Complete a peer-reviewed pull request",
        activity_steps=["Choose one assigned issue and create a focused branch.", "Make and review small commits, then push the branch.", "Open a pull request that links the issue and states validation evidence.", "Review a partner's pull request using the rubric and request one concrete improvement when needed.", "Address feedback, obtain approval, confirm checks, and merge using the approved strategy."],
        evidence="A merged pull request with linked issue, peer review, revision evidence, and passing checks",
        safety_note="Use only course repositories and never paste credentials, private student data, or secrets into issues, commits, reviews, or pull requests.",
        assessment_items=[
            ("When is a shared-branch workflow appropriate?", "When contributors have authorized write access to the same repository."),
            ("When is a fork workflow appropriate?", "When contributors do not have write access or the project requires fork-based contributions."),
            ("What should a pull-request description explain?", "Its purpose, scope, related issue, important changes, and validation evidence."),
            ("What is a pull-request diff?", "The combined change proposed from the source branch to the target branch."),
            ("What makes a useful review comment?", "A specific observation, its impact, and a clear requested outcome or question."),
            ("How is a pull request updated?", "Push additional commits to its source branch."),
            ("Why link an issue?", "It connects implementation to the requirement and can automate closure when merged."),
            ("What must happen before merge?", "Required reviews, checks, conflict resolution, and repository rules must be satisfied."),
            ("What does squash merge do?", "It combines the branch's changes into one commit on the target branch."),
            ("Why preserve review history?", "It documents decisions, feedback, revisions, and approval."),
        ],
        supplementary_readings=["GitHub Docs: About pull requests", "GitHub Docs: Reviewing proposed changes"],
        references=[GITHUB_REFERENCE, GIT_REFERENCE],
        figure_key="unit-06-pull-request-cycle",
    )


def _unit_7():
    return make_unit(
        number=7,
        title="Managing Issues and Projects",
        time_allotment="2 hours",
        overview="Students turn a need into a well-scoped issue, classify and assign it, plan it on a project board, and close it with evidence.",
        rationale="Visible work tracking helps teams agree on scope, ownership, status, and completion before code changes begin.",
        objectives=["Write an actionable issue.", "Use labels, assignees, and milestones meaningfully.", "Track work through a project workflow.", "Link implementation evidence to completion."],
        learner_instructions=["Describe an observable need.", "Write verifiable acceptance criteria.", "Update status when the work state changes."],
        materials=["Course GitHub repository", "GitHub Projects access", "Issue template"],
        discussion=[
            "An issue is a durable discussion and tracking record. A useful title names the outcome or problem; the body provides context, reproduction details when relevant, acceptance criteria, and supporting evidence.",
            "Labels classify work by type, area, priority, or status. Too many overlapping labels reduce meaning, so teams should use a small documented vocabulary.",
            "An assignee owns the next action, while a milestone groups work toward a larger target. Assignment communicates responsibility but does not replace discussion or acceptance criteria.",
            "A project view organizes issues and pull requests through states such as backlog, ready, in progress, review, and done. The board should reflect reality rather than become a second disconnected task list.",
            "Closing keywords in a pull-request description can close a linked issue after merge. The issue should contain final evidence or a link so another person can verify why it is complete.",
        ],
        command_examples=[("gh issue list", "Optional GitHub CLI view of open issues."), ("gh issue view 1", "Optional detailed issue view; replace 1 with the assigned issue number.")],
        activity_title="Track one portfolio improvement from backlog to done",
        activity_steps=["Create an issue with context and three verifiable acceptance criteria.", "Apply one type label, assign the responsible student, and add the course milestone.", "Add the issue to the project and move it from backlog to in progress.", "Link the implementing pull request and move the item to review.", "After merge, verify the acceptance criteria, close the issue, and move it to done."],
        evidence="A closed issue with label, assignee, milestone, project history, acceptance criteria, and linked implementation",
        safety_note="Do not place grades, private feedback, credentials, or personal contact information in public issues or project fields.",
        assessment_items=[
            ("What makes an issue actionable?", "A clear outcome, sufficient context, and verifiable acceptance criteria."),
            ("What should an issue title communicate?", "The specific problem or outcome in concise language."),
            ("What is the role of labels?", "They classify work using a shared vocabulary."),
            ("What does an assignee represent?", "The person responsible for the next action or completion."),
            ("What does a milestone group?", "Related issues and pull requests toward a target outcome or period."),
            ("What is a project view used for?", "To visualize and update work state across issues and pull requests."),
            ("Why should project status reflect reality?", "Accurate status lets the team coordinate and identify blocked work."),
            ("How can a pull request close an issue?", "Use a supported closing keyword with the issue reference and merge the pull request."),
            ("What evidence belongs on a completed issue?", "Links or results that demonstrate each acceptance criterion was met."),
            ("What information should public issues exclude?", "Credentials, private student data, grades, and confidential feedback."),
        ],
        supplementary_readings=["GitHub Docs: About issues", "GitHub Docs: About Projects"],
        references=[GITHUB_REFERENCE],
        figure_key="unit-07-issues-projects",
    )


def _unit_8():
    return make_unit(
        number=8,
        title="Repository and Workflow Best Practices",
        time_allotment="2 hours",
        overview="Students audit repository documentation, ignored files, commit quality, branch rules, and secret safety.",
        rationale="Consistent repository practices reduce accidental exposure, lower review cost, and help future contributors understand the project.",
        objectives=["Improve repository documentation.", "Exclude generated and sensitive files correctly.", "Evaluate commit and branch hygiene.", "Respond safely to an exposed secret."],
        learner_instructions=["Audit before editing.", "Never create a real secret for this activity.", "Explain each recommendation with evidence."],
        materials=["student-portfolio repository", "Quality checklist", "Sample unsafe repository"],
        discussion=[
            "A README should answer what the project is, why it exists, how to view or use it, and how to contribute when contributions are expected. Documentation must match the current repository rather than promise unfinished features.",
            "`.gitignore` prevents selected untracked files from being offered for commit. Common entries include `.env`, build output, dependency folders, editor state, and operating-system metadata. It does not remove files already tracked.",
            "Small commits with purposeful messages make review and recovery easier. A commit should represent one coherent change and should not mix formatting, unrelated refactoring, and new behavior without a reason.",
            "Protected collaboration keeps important branches stable by requiring pull requests, reviews, or checks. Students should pull or fetch before starting work and avoid rewriting history that other people may have based work on.",
            "A committed secret remains in history even after its latest line is deleted. The correct response begins by revoking or rotating the credential, then removing it from current files, adding ignore protection, and following the repository's approved history-cleanup procedure.",
        ],
        command_examples=[("git check-ignore -v .env", "Explains which ignore rule applies to a sensitive configuration file."), ("git ls-files .env", "Reveals whether .env is already tracked."), ("git log --oneline --graph --decorate --all", "Supports a commit-history quality audit."), ("git status --ignored", "Shows ignored paths during verification.")],
        activity_title="Conduct a repository quality and secret-safety audit",
        activity_steps=["Review README completeness and accuracy.", "Inspect .gitignore for environment, build, editor, and OS artifacts.", "Review ten recent commits for scope and message quality.", "Check whether the default-branch workflow requires review or automated checks.", "Analyze a fictional exposed-token scenario and write the revoke-first response sequence."],
        evidence="A prioritized repository audit with evidence and corrected README and ignore rules",
        safety_note="Use only fictional credential strings. If a real secret is discovered, stop sharing it, revoke it immediately, notify the instructor or owner, and follow the approved incident process.",
        assessment_items=[
            ("What should a README establish?", "Project purpose, use or viewing instructions, current scope, and contribution guidance when relevant."),
            ("What does .gitignore affect?", "It affects untracked paths that Git should ignore; it does not remove already tracked files."),
            ("Why ignore .env?", "It commonly contains environment-specific configuration and secrets that should not enter version history."),
            ("What makes a commit focused?", "Its changes serve one coherent purpose that can be explained and reviewed together."),
            ("Why protect the default branch?", "To require review and validation before shared production history changes."),
            ("Why avoid rewriting shared history?", "Other collaborators may have based work on commit identifiers that rewriting replaces."),
            ("What is the first response to an exposed token?", "Revoke or rotate the credential so the exposed value no longer grants access."),
            ("Does deleting a secret in a new commit erase history?", "No. Earlier commits still contain the value."),
            ("What does git check-ignore -v explain?", "The matching ignore rule and file responsible for it."),
            ("What should an audit recommendation contain?", "A specific finding, evidence, impact, and prioritized corrective action."),
        ],
        supplementary_readings=["GitHub Docs: Ignoring files", "GitHub Docs: Removing sensitive data from a repository"],
        references=[GITHUB_REFERENCE, GIT_REFERENCE],
        figure_key="unit-08-healthy-repository",
    )


def _unit_9():
    workflow = """# .github/workflows/validate.yml
name: Validate portfolio
on: [push, pull_request]
permissions:
  contents: read
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Verify required files
        shell: bash
        run: test -f README.md && test -f index.html"""
    return make_unit(
        number=9,
        title="GitHub Actions and Automation",
        time_allotment="3 hours",
        overview="Students create a least-privilege workflow that validates required portfolio files on pushes and pull requests.",
        rationale="Automated checks provide repeatable feedback before changes are merged or published.",
        objectives=["Identify workflow events, jobs, runners, steps, and actions.", "Create a valid workflow file.", "Interpret workflow logs and results.", "Apply least-privilege permissions and secret safety."],
        learner_instructions=["Create the file under .github/workflows.", "Use YAML spaces consistently.", "Read the failed step before changing the workflow."],
        materials=["student-portfolio repository", "GitHub Actions access", "Text editor"],
        discussion=[
            "A GitHub Actions workflow is a YAML file stored under `.github/workflows`. Repository events such as push or pull_request can trigger one or more jobs.",
            "A job runs on a selected runner and contains ordered steps. A step may run a shell command or invoke a reusable action. Jobs are isolated unless artifacts or outputs are passed deliberately.",
            "The workflow should request only the permissions it needs. A validation job that reads repository files can normally use `contents: read` rather than write access.",
            "A failed run is diagnostic evidence. Students should open the job, find the first failed step, read its command and output, reproduce the condition when possible, then make a focused correction.",
            "Secrets belong in GitHub's encrypted secret storage and are accessed through the secrets context. Secret values must not be printed, committed, placed in screenshots, or copied into workflow source.",
        ],
        command_examples=[(workflow, "A complete least-privilege validation workflow for the portfolio repository."), ("git add .github/workflows/validate.yml", "Stages the workflow definition."), ('git commit -m "ci: validate portfolio files"', "Records the automation as a focused change."), ("git push", "Publishes the workflow and triggers the push event.")],
        activity_title="Create a portfolio validation workflow",
        activity_steps=["Create .github/workflows/validate.yml using the supplied structure.", "Commit and push the workflow on a feature branch.", "Inspect the run and identify its trigger, job, runner, and steps.", "Temporarily rename one required file in the practice branch, observe the expected failure, and read the log.", "Restore the file, push the correction, obtain a passing run, and open a pull request."],
        evidence="A workflow file, one explained failure, a corrected passing run, and a pull request check",
        safety_note="Never place a real secret in YAML, logs, commands, commits, screenshots, or assessment evidence. Use repository secret storage only when an approved activity requires it.",
        assessment_items=[
            ("Where must workflow files be stored?", "In the repository's .github/workflows directory with a .yml or .yaml extension."),
            ("What starts a workflow run?", "A configured event, schedule, manual dispatch, or other supported trigger."),
            ("What is a job?", "A set of steps executed on the same runner."),
            ("What is a runner?", "The machine environment that executes a workflow job."),
            ("What can a step do?", "Run a shell command or use a reusable action."),
            ("Why declare permissions?", "To limit the workflow token to the access the job actually requires."),
            ("What should be inspected first after failure?", "The first failed step and its command output."),
            ("Where should approved secret values be stored?", "In GitHub's encrypted secrets store, not in the workflow file."),
            ("What triggers the example workflow?", "Push and pull_request events."),
            ("What does a passing check demonstrate?", "That the defined automated conditions succeeded for that commit; it does not prove every possible defect is absent."),
        ],
        supplementary_readings=["GitHub Docs: Quickstart for GitHub Actions", "GitHub Docs: Workflow syntax"],
        references=[GITHUB_REFERENCE],
        figure_key="unit-09-actions-pipeline",
    )
