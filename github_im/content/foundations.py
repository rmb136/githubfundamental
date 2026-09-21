from __future__ import annotations

from .common import GITHUB_REFERENCE, GIT_REFERENCE, make_unit


def build_foundation_units():
    return [_unit_1(), _unit_2(), _unit_3(), _unit_4()]


def _unit_1():
    return make_unit(
        number=1,
        title="Introduction to Git and GitHub",
        time_allotment="2 hours",
        overview="This unit builds the mental model used throughout the module: files begin in a working tree, selected versions enter the staging area, commits form local history, and a remote repository supports sharing.",
        rationale="Students who understand the states of a change can interpret Git messages, choose commands deliberately, and recover from mistakes instead of memorizing unexplained command sequences.",
        objectives=[
            "Differentiate Git, GitHub, and an ordinary file-storage service.",
            "Identify a repository, commit, branch, clone, and remote in a development workflow.",
            "Trace a file change from the working tree through the staging area and local history to a remote.",
            "Explain how version history supports accountability, collaboration, and recovery.",
        ],
        learner_instructions=[
            "Complete the pre-test without consulting notes.",
            "Use the student-portfolio example when drawing the workflow.",
            "Describe each arrow in the concept map with an action and resulting state.",
        ],
        materials=["Computer or paper for diagramming", "Web browser", "This module"],
        discussion=[
            "Version control records meaningful states of a project over time. Unlike a sequence of folders named final, final-2, and final-revised, a repository preserves ordered snapshots with messages, authorship, and relationships among changes.",
            "Git is the version control system that operates on a local computer. GitHub hosts Git repositories and adds pull requests, issues, projects, automation, access controls, and web publishing. Git can be used without GitHub, and GitHub also provides features beyond Git itself.",
            "A repository is the project working tree plus the hidden Git database that stores objects and references. A commit records the exact staged content, a message, author information, time, and a link to its parent commit or commits.",
            "The staging area is a deliberate checkpoint between editing and committing. It lets a student choose which completed changes belong together. Unstaged work remains in the working tree; staged content is proposed for the next commit; committed content belongs to local history.",
            "A branch is a movable name pointing to a commit. Branches let people develop changes without immediately altering the default branch. A remote is a named connection to another repository; `origin` is the conventional name assigned when cloning.",
            "Cloning creates a local repository with history and a configured remote. Pushing transfers local commits to a remote. Fetching downloads remote history without integrating it, while pulling fetches and then integrates according to configuration.",
        ],
        command_examples=[
            ("git status", "Reports the current branch and the state of working-tree and staged changes."),
            ("git log --oneline", "Shows a compact view of recorded commits."),
        ],
        activity_title="Map the life of a change",
        activity_steps=[
            "Draw four labeled zones: working tree, staging area, local repository, and GitHub remote.",
            "Place a README.md change in the working tree and show how add, commit, and push move its selected state.",
            "Add reverse arrows for fetch and pull, and explain that fetch alone does not edit the current working files.",
            "Compare the map with a partner and correct any arrow that skips a required state.",
        ],
        evidence="An annotated concept map with four states and accurate action arrows",
        safety_note="Use a fictional project name and omit account credentials from the diagram.",
        assessment_items=[
            ("What problem does version control solve?", "It records ordered project states so changes can be explained, compared, shared, and recovered."),
            ("How does Git differ from GitHub?", "Git is the local distributed version control system; GitHub is a hosted collaboration platform built around Git repositories."),
            ("What does a commit contain?", "A commit records staged content, metadata, and links to its parent history."),
            ("What is the staging area?", "It is the index holding the exact content proposed for the next commit."),
            ("What is a branch?", "A branch is a movable name that points to a line of commits."),
            ("What does cloning create?", "It creates a local repository with project files, history, and a configured remote."),
            ("Why use a remote repository?", "A remote supports sharing, backup, collaboration, review, and automation."),
            ("What is the working tree?", "It is the checked-out set of files currently available for editing."),
            ("What is the difference between fetch and pull?", "Fetch downloads remote history without integrating it; pull fetches and then integrates."),
            ("Why are descriptive commit messages useful?", "They explain the purpose of a recorded change to reviewers and future maintainers."),
        ],
        supplementary_readings=["Git reference: Getting Started", "GitHub Docs: About Git"],
        references=[GIT_REFERENCE, GITHUB_REFERENCE],
        figure_key="unit-01-version-control-flow",
    )


def _unit_2():
    return make_unit(
        number=2,
        title="Setting Up Git and GitHub",
        time_allotment="2 hours",
        overview="This unit prepares a secure working environment by installing Git, configuring commit identity, creating a GitHub account, and selecting an authentication method.",
        rationale="A correct setup prevents unattributed commits, failed pushes, and unsafe credential handling during later activities.",
        objectives=[
            "Install Git and verify the installed version.",
            "Configure and inspect the name and email recorded in commits.",
            "Compare HTTPS and SSH authentication for student use.",
            "Verify GitHub access without exposing a password, token, or private key.",
        ],
        learner_instructions=[
            "Follow the installation path approved for the laboratory computer.",
            "Use the name and email directed by the instructor.",
            "Redact personal information before submitting terminal output.",
        ],
        materials=["Computer with installation permission", "GitHub account", "Internet connection"],
        discussion=[
            "Git is available for Windows, macOS, and Linux. Installation methods differ, but verification is consistent: the `git --version` command should report an installed release rather than an unrecognized command.",
            "Git records a user name and email in each commit. These values identify authorship; they are not login credentials. A student may use a verified GitHub email or a GitHub-provided no-reply address when privacy is important.",
            "Global configuration applies to repositories for the current operating-system account. Repository-local configuration can override it when a course or workplace requires a different identity. Students should inspect effective values before the first commit.",
            "HTTPS and SSH are both valid remote protocols. HTTPS commonly uses a credential manager or personal access token. SSH uses a public/private key pair. The public key may be registered with GitHub; the private key remains only on the student's device.",
            "Authentication proves access to GitHub, while authorization determines what the account may do. A successful account login does not automatically permit writes to every repository.",
            "Security evidence should demonstrate a successful connection without revealing credentials. A screenshot must exclude password fields, token values, recovery codes, private-key content, and unrelated personal information.",
        ],
        command_examples=[
            ("git --version", "Verifies that Git is installed and available on PATH."),
            ('git config --global user.name "Student Name"', "Sets the author name for new commits."),
            ('git config --global user.email "student@example.edu"', "Sets the author email for new commits."),
            ("git config --global --list", "Displays global configuration for review; redact private values before submission."),
            ("ssh -T git@github.com", "Tests SSH authentication after a public key is registered; no repository data is changed."),
        ],
        activity_title="Configure and verify the development identity",
        activity_steps=[
            "Run git --version and record the reported version.",
            "Configure the instructor-approved name and email.",
            "Inspect the effective configuration and correct typographical errors.",
            "Choose HTTPS with a credential manager or SSH with a protected private key.",
            "Verify access and submit only redacted evidence of success.",
        ],
        evidence="Git version, redacted identity configuration, and verified GitHub access",
        safety_note="Never submit a password, personal access token, recovery code, or private key. Submit only redacted verification output.",
        assessment_items=[
            ("How do you verify a Git installation?", "Run git --version and confirm that it reports an installed version."),
            ("What does user.name control?", "It supplies the author name recorded in new commits."),
            ("What does user.email control?", "It supplies the author email recorded in new commits and can link commits to a verified GitHub identity."),
            ("Is the Git email a login password?", "No. It is commit metadata, not a credential."),
            ("What is the difference between global and local configuration?", "Global values apply to the current user by default; local values apply only to one repository and override global values."),
            ("What is safe to upload from an SSH key pair?", "Only the public key; the private key must remain protected on the device."),
            ("How does HTTPS commonly authenticate Git operations?", "It uses a credential manager or token-based credential rather than an account password."),
            ("What should be redacted from setup evidence?", "Tokens, passwords, private keys, recovery codes, and unrelated personal data."),
            ("Why verify identity before the first commit?", "Because correcting authorship after commits are shared may require history rewriting."),
            ("What does a successful authentication test prove?", "It proves the credential identifies the account; repository permissions still determine allowed actions."),
        ],
        supplementary_readings=["Git reference: git-config", "GitHub Docs: Connecting to GitHub with SSH"],
        references=[GIT_REFERENCE, GITHUB_REFERENCE],
        figure_key="unit-02-setup-authentication",
    )


def _unit_3():
    return make_unit(
        number=3,
        title="Creating the First Repository",
        time_allotment="2 hours",
        overview="Students create the continuing student-portfolio repository, inspect its remote connection, record an initial README, and publish the first commit.",
        rationale="A small, well-documented repository provides a safe workspace for every later branching, collaboration, automation, and publishing exercise.",
        objectives=[
            "Create and clone a GitHub repository using a beginner-safe workflow.",
            "Initialize a local repository and connect it to a remote when required.",
            "Record an initial README in a focused commit.",
            "Verify the remote and publish the default branch.",
        ],
        learner_instructions=[
            "Use the repository name student-portfolio unless the instructor assigns another name.",
            "Do not initialize the same directory twice.",
            "Check status after every major step.",
        ],
        materials=["Configured Git installation", "GitHub account", "Text editor"],
        discussion=[
            "A repository can begin remotely or locally. For beginners, creating a GitHub repository with a README and then cloning it reduces remote-configuration mistakes. Existing local work can instead be initialized and connected to an empty remote.",
            "Cloning creates a new project directory, copies Git history, checks out the default branch, and creates the `origin` remote. Students should not clone into a directory that already contains unrelated work.",
            "Initializing with `git init` creates the local Git database but does not create a GitHub repository or upload files. A remote must be added deliberately, and the local branch name should match the intended default branch.",
            "A README explains the project's purpose, current contents, and how another reader can understand or use it. The initial README should be brief, accurate, and free of private student information.",
            "The first commit establishes a meaningful baseline. `git status` should be read before staging and again after committing so the student observes how the repository state changes.",
            "The upstream link created by `git push -u origin main` lets later `git push` and `git pull` commands infer the associated remote branch. The command succeeds only when authentication and permissions are valid.",
        ],
        command_examples=[
            ("git clone https://github.com/ACCOUNT/student-portfolio.git", "Creates a local copy and configures origin. Replace ACCOUNT with the actual account name."),
            ("git init", "Initializes Git in the current directory for the alternate local-first path."),
            ("git branch -M main", "Names the current branch main before the first push in the local-first path."),
            ("git remote add origin https://github.com/ACCOUNT/student-portfolio.git", "Connects a local repository to its GitHub remote."),
            ("git remote -v", "Displays fetch and push URLs for configured remotes."),
            ("git add README.md", "Stages the README content for the next commit."),
            ('git commit -m "docs: add initial project overview"', "Records the initial documented state."),
            ("git push -u origin main", "Publishes main and records its upstream remote branch."),
        ],
        activity_title="Create and publish student-portfolio",
        activity_steps=[
            "Create the repository on GitHub with the visibility directed by the instructor and include a README.",
            "Clone the repository, enter its directory, and inspect git status and git remote -v.",
            "Add a purpose statement and learning-goals section to README.md.",
            "Stage only README.md, commit with a descriptive message, and push.",
            "Confirm on GitHub that the commit and README are visible.",
        ],
        evidence="Repository URL or approved screenshot plus redacted git log --oneline output",
        safety_note="Do not publish student numbers, home addresses, passwords, tokens, private keys, or confidential course data.",
        assessment_items=[
            ("What does git clone create?", "A local repository with project files, history, a checked-out branch, and an origin remote."),
            ("What does git init create?", "It creates a local Git repository in the current directory; it does not create or upload a GitHub repository."),
            ("Why inspect git remote -v?", "It confirms the repository's fetch and push destinations before synchronization."),
            ("What belongs in the first README?", "A clear purpose, scope, and basic project information without private data."),
            ("Why check status before committing?", "It confirms that only intended changes are staged and reveals untracked or unstaged files."),
            ("What does origin mean?", "It is the conventional name for the primary remote, commonly created by cloning."),
            ("What does -u do on the first push?", "It records the upstream relationship between the local and remote branch."),
            ("Why might a push be rejected?", "Authentication, authorization, branch rules, an incorrect remote, or remote commits not present locally can cause rejection."),
            ("What is the safer beginner repository-start path?", "Create the remote with a README and clone it, because the remote and default branch are configured automatically."),
            ("What should repository evidence exclude?", "Secrets and unnecessary personal information."),
        ],
        supplementary_readings=["GitHub Docs: Quickstart for repositories", "Git reference: git-clone and git-init"],
        references=[GIT_REFERENCE, GITHUB_REFERENCE],
        figure_key="unit-03-repository-lifecycle",
    )


def _unit_4():
    return make_unit(
        number=4,
        title="Essential Git Commands",
        time_allotment="2 hours",
        overview="This unit turns individual commands into a repeatable edit, inspect, stage, review, commit, and synchronize workflow.",
        rationale="A disciplined cycle produces focused commits, reduces accidental changes, and gives students reliable checkpoints for later collaboration.",
        objectives=[
            "Inspect working-tree and staging-area state before recording changes.",
            "Stage selected content and review its diff.",
            "Create focused commits with descriptive messages.",
            "Synchronize local and remote history using fetch, pull, and push deliberately.",
        ],
        learner_instructions=[
            "Run status before and after each state-changing command.",
            "Commit one coherent change at a time.",
            "Read command output instead of assuming success.",
        ],
        materials=["student-portfolio repository", "Text editor", "Terminal"],
        discussion=[
            "`git status` is the primary orientation command. It reports the current branch, upstream relationship, staged changes, unstaged changes, and untracked files. A clean status means the working tree matches the current commit.",
            "`git diff` shows unstaged changes by default. `git diff --staged` shows the exact content proposed for the next commit. Reviewing both prevents unrelated edits or debugging output from entering history.",
            "`git add` copies selected file content into the staging area. It does not permanently save a version and it does not upload anything. Editing a file after staging creates a staged version and a newer unstaged version, which status displays separately.",
            "`git commit` creates a local history entry from staged content. A strong message begins with a concise action and explains one coherent purpose, such as `docs: add skills section to portfolio`.",
            "`git log --oneline --graph --decorate` reveals commit order, branch labels, and merges. Students should use the history to verify that a requested commit exists rather than relying only on the final files.",
            "`git fetch` updates remote-tracking information without changing the current branch. `git pull` fetches and integrates. `git push` publishes local commits. Inspecting status and history before synchronization makes unexpected divergence easier to diagnose.",
        ],
        command_examples=[
            ("git status", "Orient before choosing the next command."),
            ("git diff", "Review unstaged line changes."),
            ("git add README.md", "Stage one file deliberately."),
            ("git diff --staged", "Review the exact staged content."),
            ('git commit -m "docs: add portfolio skills"', "Record one coherent change in local history."),
            ("git log --oneline --graph --decorate", "Inspect compact history and branch labels."),
            ("git fetch origin", "Download remote history without integrating it."),
            ("git pull --ff-only", "Update only when a fast-forward is possible, avoiding an accidental merge commit."),
            ("git push", "Publish commits to the configured upstream branch."),
        ],
        activity_title="Build a three-commit learning history",
        activity_steps=[
            "Add an About section to README.md, inspect the diff, stage it, review the staged diff, and commit.",
            "Add a Skills section and record it as a second focused commit.",
            "Add a Contact section using only instructor-approved public information and record a third focused commit.",
            "Inspect the graph, push the commits, and verify that status reports a clean working tree.",
        ],
        evidence="A three-commit git log and a clean git status after push",
        safety_note="Use only public contact information approved for the activity; do not commit private addresses, passwords, tokens, or keys.",
        assessment_items=[
            ("What does git status report?", "It reports branch and upstream state plus staged, unstaged, and untracked changes."),
            ("What does git diff show by default?", "It shows unstaged changes between the working tree and staging area."),
            ("What does git diff --staged show?", "It shows the content staged for the next commit compared with the current commit."),
            ("What does git add do?", "It copies selected current file content into the staging area."),
            ("What does git commit do?", "It records staged content as a new local commit with metadata and a parent relationship."),
            ("Why create focused commits?", "They make changes easier to review, explain, test, revert, and combine."),
            ("What does git fetch change?", "It updates remote-tracking data without integrating changes into the current branch."),
            ("How does pull differ from fetch?", "Pull fetches and then integrates; fetch only downloads remote history."),
            ("When is git push used?", "After local commits are ready to publish to an authorized remote branch."),
            ("What does a clean working tree mean?", "Tracked files match the current commit and no staged or unstaged changes remain."),
        ],
        supplementary_readings=["Git reference: Everyday Git", "GitHub Docs: Pushing commits to a remote repository"],
        references=[GIT_REFERENCE, GITHUB_REFERENCE],
        figure_key="unit-04-command-flow",
    )
