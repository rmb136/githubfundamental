from __future__ import annotations

from .common import GITHUB_REFERENCE, GIT_REFERENCE, make_unit


def build_publishing_units():
    return [_unit_10(), _unit_11(), _unit_12(), _unit_13()]


def _unit_10():
    return make_unit(
        number=10,
        title="GitHub Pages and Static-Site Publishing",
        time_allotment="3 hours",
        overview="Students turn the continuing portfolio repository into a public static site and verify its deployment.",
        rationale="Publishing makes repository content visible to an authentic audience and connects version control with a repeatable deployment process.",
        objectives=["Explain what GitHub Pages can publish.", "Create a valid entry page.", "Configure a publishing source.", "Diagnose a failed or stale deployment."],
        learner_instructions=["Publish only instructor-approved content.", "Use relative links for project files.", "Verify the deployed URL in a private browser window."],
        materials=["student-portfolio repository", "Web browser", "Text editor"],
        discussion=[
            "GitHub Pages publishes static HTML, CSS, JavaScript, and assets from a repository. It does not run a general server-side application or protect content behind course authentication.",
            "A project site needs a clear entry point such as `index.html`. Relative paths keep styles, images, and internal links working when the site is served below an account and repository path.",
            "Repository settings identify the publishing source. Depending on the repository, Pages can deploy from a selected branch and folder or through a GitHub Actions workflow.",
            "A deployment has its own status and logs. A successful commit does not guarantee a successful publication; students should inspect the Pages deployment and the browser result.",
            "Publishing requires a privacy review. A portfolio must not expose student numbers, home addresses, private contact details, grades, credentials, unpublished assessments, or copyrighted material without permission.",
        ],
        command_examples=[
            ("test -f index.html", "Checks that the required entry page exists in a Unix-like shell."),
            ("git add index.html assets/", "Stages the site entry page and intended assets."),
            ('git commit -m "feat: publish portfolio landing page"', "Records the site as a focused change."),
            ("git push", "Publishes the commit so the configured Pages source can deploy it."),
        ],
        activity_title="Publish the student portfolio",
        activity_steps=["Create index.html with a title, short introduction, skills list, and links to approved project work.", "Run a privacy review and remove personal or confidential information.", "Commit and push the static site on a reviewed branch.", "Configure the repository's GitHub Pages source and inspect deployment status.", "Open the public URL, test every link, and record one corrected publishing issue if present."],
        evidence="A working GitHub Pages URL, deployment status, privacy checklist, and verified navigation",
        safety_note="Publish only instructor-approved public information; never publish credentials, private student records, home addresses, or copyrighted material without permission.",
        assessment_items=[
            ("What type of content does GitHub Pages publish?", "Static web content such as HTML, CSS, JavaScript, and assets."),
            ("What entry file is commonly required?", "An index.html file at the configured publishing source."),
            ("Why prefer relative links?", "They continue to work when the project site is served beneath a repository-specific path."),
            ("Where is the publishing source selected?", "In the repository's Pages settings or through a configured Pages workflow."),
            ("Does a successful push prove deployment succeeded?", "No. The Pages deployment status and public URL must also be checked."),
            ("What should deployment logs be used for?", "To identify the failing build or publication step and its error message."),
            ("What content must a student portfolio exclude?", "Credentials, private records, home addresses, grades, and material lacking publication permission."),
            ("Why test in a private browser window?", "It helps verify that the public site works without relying on a signed-in session."),
            ("What should be checked after publication?", "The URL, page content, navigation, assets, privacy, and deployment status."),
            ("What does static hosting not provide?", "A general server-side runtime or private course access control."),
        ],
        supplementary_readings=["GitHub Docs: Quickstart for GitHub Pages", "GitHub Docs: Configuring a publishing source"],
        references=[GITHUB_REFERENCE],
        figure_key="unit-10-pages-publishing",
    )


def _unit_11():
    return make_unit(
        number=11,
        title="Security and Advanced GitHub Features",
        time_allotment="2 hours",
        overview="Students audit account and repository protections and survey releases, packages, insights, and API-based automation.",
        rationale="Security and advanced features are most useful when students understand access boundaries, alerts, and the limits of each capability.",
        objectives=["Apply account and repository security controls.", "Interpret dependency and code-security findings.", "Explain releases, packages, insights, and API use cases.", "Prioritize repository improvements using risk and effort."],
        learner_instructions=["Use a sample repository for the audit.", "Do not enable paid features for this activity.", "Separate observed evidence from recommendations."],
        materials=["GitHub account", "Sample repository", "Security audit checklist"],
        discussion=[
            "Account security begins with a unique password, two-factor authentication, protected recovery methods, and careful review of authorized applications and active sessions.",
            "Least privilege means granting each collaborator, workflow, token, and integration only the access required for its task. Access should be reviewed when roles or projects change.",
            "Secret scanning can identify supported credential patterns, while push protection may block known secret formats before they enter history. Detection does not replace immediate revocation of an exposed credential.",
            "Dependabot alerts identify known vulnerabilities in supported dependencies, and dependency review explains changes introduced by a pull request. Code scanning analyzes code for configured classes of security weakness.",
            "Tags and releases mark meaningful versions; Packages distributes supported artifacts; Insights summarizes repository activity; and the GitHub API enables authorized automation. These features should solve a defined need rather than be enabled for decoration.",
        ],
        command_examples=[("git tag -a v1.0.0 -m \"Release portfolio version 1.0.0\"", "Creates an annotated local release tag."), ("git push origin v1.0.0", "Publishes the approved tag."), ("gh api repos/OWNER/REPOSITORY", "Optional authenticated API request for repository metadata; replace placeholders and never expose a token.")],
        activity_title="Audit repository security and advanced-feature readiness",
        activity_steps=["Confirm two-factor authentication is enabled without capturing recovery codes.", "Review collaborators and workflow permissions for least privilege.", "Inspect available dependency, secret, and code-scanning findings.", "Evaluate whether a release, package, insight, or API use case serves the portfolio project.", "Recommend three improvements ranked by risk reduction, learning value, and implementation effort."],
        evidence="A redacted security audit with three prioritized and justified improvements",
        safety_note="Do not include passwords, tokens, private keys, recovery codes, private alerts, or sensitive repository content in submitted evidence.",
        assessment_items=[
            ("Why enable two-factor authentication?", "It requires a second factor and reduces risk from a stolen password."),
            ("What is least privilege?", "Granting only the access needed for a specific task and duration."),
            ("What should happen after a real secret is exposed?", "Revoke or rotate it immediately, then follow the incident and cleanup process."),
            ("What do Dependabot alerts report?", "Known vulnerabilities affecting supported dependencies in the repository."),
            ("What does dependency review show?", "Dependency changes and risk information introduced by a pull request."),
            ("What does code scanning analyze?", "Source code for configured patterns of security weakness."),
            ("What is an annotated tag used for?", "To give a durable name and metadata to a specific commit, often for a release."),
            ("What is GitHub Packages for?", "Publishing and consuming supported software packages or container artifacts."),
            ("What can Insights provide?", "Views of repository activity, contributors, traffic, dependencies, and related metrics when available."),
            ("When should the GitHub API be used?", "When an authorized, repeatable integration or automation has a defined need."),
        ],
        supplementary_readings=["GitHub Docs: Securing your account", "GitHub Docs: Securing your repository"],
        references=[GITHUB_REFERENCE, GIT_REFERENCE],
        figure_key="unit-11-security-layers",
    )


def _unit_12():
    return make_unit(
        number=12,
        title="Contributing to Open Source Projects",
        time_allotment="2 hours",
        overview="Students prepare a respectful, policy-compliant contribution using project documentation, a focused branch, and review feedback.",
        rationale="Open-source contribution combines technical Git skills with licensing awareness, community norms, and clear communication.",
        objectives=["Evaluate whether a project welcomes a proposed contribution.", "Follow repository community and contribution files.", "Prepare a focused fork-based change.", "Respond constructively to maintainer review."],
        learner_instructions=["Use only an instructor-approved project.", "Read community files before editing.", "Do not claim an issue without following project norms."],
        materials=["Instructor-approved repository", "GitHub account", "Contribution checklist"],
        discussion=[
            "A suitable first contribution has clear scope, active maintainers, an understandable contribution guide, and a license. Documentation corrections and small tests often provide a safer entry than a large feature.",
            "README, CONTRIBUTING, CODE_OF_CONDUCT, issue templates, pull-request templates, and license files define how a community expects work to proceed. Repository-specific rules override generic advice.",
            "A fork creates a contributor-owned remote copy. The contributor clones the fork, adds the original repository as `upstream`, synchronizes from upstream, and creates a focused branch for the proposed change.",
            "A good contribution explains motivation, limits its diff, includes validation evidence, and avoids unrelated cleanup. Licensing and attribution requirements must be respected for any reused material.",
            "Maintainer feedback is part of the contribution. Contributors should ask clarifying questions, update the same pull request with focused commits, and accept that maintainers may decline work that does not fit the project.",
        ],
        command_examples=[("git remote add upstream https://github.com/ORIGINAL/PROJECT.git", "Connects the local clone to the original repository."), ("git fetch upstream", "Downloads the original repository's current history."), ("git switch -c docs/clarify-setup upstream/main", "Creates a focused contribution branch from current upstream main."), ("git push -u origin docs/clarify-setup", "Publishes the branch to the contributor's fork.")],
        activity_title="Prepare an open-source contribution",
        activity_steps=["Select an instructor-approved project and read its README, contribution guide, code of conduct, and license.", "Identify one small issue or documentation improvement and confirm that it is not already being addressed.", "Fork, clone, add upstream, synchronize, and create a focused branch.", "Make the smallest complete change and validate it according to project instructions.", "Prepare a pull-request description or submit the contribution when the instructor authorizes external interaction."],
        evidence="A contribution plan or documentation pull request that follows the project's stated policies",
        safety_note="Do not submit to an external project without instructor approval, and never include credentials, private course work, or copyrighted content without permission.",
        assessment_items=[
            ("What makes a project suitable for a first contribution?", "Clear scope, active maintenance, understandable contribution guidance, and a license."),
            ("Which repository files should be read first?", "README, contribution guide, code of conduct, templates, and license."),
            ("What is a fork?", "A GitHub-hosted copy under another account for independent contribution work."),
            ("What is the upstream remote?", "A local remote name conventionally pointing to the original project repository."),
            ("Why synchronize before branching?", "To base the contribution on current project history and reduce conflicts."),
            ("What makes a contribution focused?", "It solves one agreed problem without unrelated changes."),
            ("Why check the license?", "It defines permissions and obligations for using and contributing material."),
            ("How should review feedback be handled?", "Clarify respectfully, make focused revisions, and update the same pull request."),
            ("Can a maintainer decline a technically correct change?", "Yes. It may not fit project scope, timing, design, or maintenance priorities."),
            ("What requires instructor approval in this unit?", "Any actual interaction or submission to an external project."),
        ],
        supplementary_readings=["GitHub Docs: Contributing to open source", "Open Source Guides: How to Contribute"],
        references=[GITHUB_REFERENCE, "GitHub. (2026). Open Source Guides. https://opensource.guide/"],
        figure_key="unit-12-open-source-contribution",
    )


def _unit_13():
    return make_unit(
        number=13,
        title="Troubleshooting and Recovery",
        time_allotment="3 hours",
        overview="Students diagnose repository state before choosing a safe repair and document what evidence justified the action.",
        rationale="Recovery becomes safer when students observe first, preserve work, choose the least destructive action, and verify the result.",
        objectives=["Collect diagnostic evidence before repair.", "Resolve common synchronization and authentication failures.", "Recover staged, working-tree, and committed work safely.", "Explain when destructive history operations require escalation."],
        learner_instructions=["Stop after an unexpected result.", "Copy important uncommitted files before risky recovery.", "Use the least destructive command that solves the diagnosed problem."],
        materials=["Instructor-provided broken repositories", "Terminal", "Recovery decision sheet"],
        discussion=[
            "Troubleshooting begins with the exact command, complete error, current branch, status, recent log, remote URLs, and any action immediately before failure. Guessing with random commands can destroy the evidence needed for recovery.",
            "A rejected push often means remote history has commits not present locally or branch rules require a pull request. Fetch, inspect the graph, and choose an approved integration path rather than forcing the push.",
            "Authentication failures require checking the remote protocol, credential helper or SSH agent, account access, token scope, and repository permission. If a credential is exposed, revoke it before continuing.",
            "`git restore` can discard an unwanted working-tree edit or unstage content depending on its options. `git revert` records a new commit that reverses an earlier commit and is usually safer for shared history than rewriting it.",
            "`git reflog` records recent local reference movement and can help locate an apparently lost commit. A detached HEAD can be preserved by creating a branch at the valuable commit before switching away.",
            "`git reset --hard` and force-push can permanently discard reachable work or replace shared history. They belong only in an instructor-led recovery after a backup, diagnosis, communication, and confirmation that safer alternatives are insufficient.",
        ],
        command_examples=[("git status", "Captures branch and file state before repair."), ("git log --oneline --graph --decorate --all -15", "Shows recent local and remote-tracking history."), ("git remote -v", "Confirms the actual fetch and push destinations."), ("git reflog -15", "Locates recent local branch and HEAD movement."), ("git restore --staged FILE", "Unstages a file while preserving its working-tree content."), ("git restore FILE", "Discards an unwanted working-tree change after verification and backup."), ("git revert COMMIT", "Creates a new commit that reverses a shared change."), ("git switch -c recovered-work COMMIT", "Preserves a valuable commit by creating a branch."), ("git reset --hard COMMIT", "Instructor-led last resort that resets index and working tree and can discard work."),
        ],
        activity_title="Diagnose and recover four controlled failures",
        activity_steps=["For each broken practice repository, record the command, error, status, graph, and remote configuration.", "Classify the problem as authentication, synchronization, conflict, detached HEAD, staging, or recovery.", "Choose the least destructive repair and predict its effect on working tree, index, history, and remote.", "Apply the repair, verify status and history, and record evidence.", "Compare the safe solution with an instructor-demonstrated destructive alternative and explain why escalation is required."],
        evidence="A four-case troubleshooting log showing evidence, diagnosis, selected repair, predicted effect, and verified result",
        safety_note="Never use reset --hard, force push, or another history rewrite outside an instructor-led practice repository. Make a backup first and confirm that the command cannot affect shared work.",
        assessment_items=[
            ("What evidence should be collected first?", "The exact command and error, status, branch, recent graph, remote URLs, and preceding action."),
            ("Why fetch before repairing a rejected push?", "It reveals remote history without immediately changing the current branch."),
            ("What should happen if a credential was exposed?", "Revoke or rotate it immediately before repository cleanup."),
            ("How can staged content be unstaged safely?", "Use git restore --staged FILE while keeping the working-tree content."),
            ("When is git restore FILE dangerous?", "When the current working-tree changes are valuable and not backed up, because the command discards them."),
            ("Why is git revert suitable for shared history?", "It preserves existing commits and records a new inverse change."),
            ("What does git reflog help locate?", "Recent local reference and HEAD positions, including commits no longer named by a branch."),
            ("How can detached work be preserved?", "Create a new branch pointing to the valuable commit before switching away."),
            ("Why is force-push risky?", "It can replace remote history that collaborators depend on."),
            ("When is reset --hard acceptable in this module?", "Only as an instructor-led last resort in a backed-up practice repository after safer options are rejected."),
        ],
        supplementary_readings=["Git reference: git-restore", "Git reference: git-reflog", "GitHub Docs: Troubleshooting connectivity problems"],
        references=[GIT_REFERENCE, GITHUB_REFERENCE],
        figure_key="unit-13-troubleshooting-path",
    )
