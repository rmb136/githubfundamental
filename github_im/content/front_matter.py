from __future__ import annotations


def build_front_matter() -> dict[str, object]:
    preface = [
        "GitHub Fundamentals for Beginners is a semester learning module for BSIT students who are new to version control, command-line Git, and collaborative development on GitHub. It begins with a concrete model of how files move from a working folder into a recorded history, then develops the skills needed to collaborate, automate checks, publish a static site, and recover from common mistakes.",
        "The module uses one continuing student-portfolio project so that every activity contributes to a visible body of work. Students should complete the diagnostic questions before reading each unit, follow the guided activity in a practice repository, and submit only the evidence named in the performance task. Private keys, access tokens, passwords, and other secrets must never be submitted.",
    ]
    glossary = {
        "Action": "A reusable task that runs as a step in a GitHub Actions workflow.",
        "Authentication": "The process of proving identity to GitHub or another remote service.",
        "Branch": "A movable name that points to a line of commits.",
        "Clone": "A local copy of a repository that includes its history and remote connection.",
        "Code review": "A structured examination of proposed changes before they are merged.",
        "Commit": "A recorded snapshot of staged changes with author, time, and message metadata.",
        "Commit hash": "A unique identifier for a commit object.",
        "Conflict": "A situation in which Git cannot automatically combine competing changes.",
        "Continuous integration": "Automated validation of changes whenever selected repository events occur.",
        "Default branch": "The branch GitHub presents as the repository's primary line of development.",
        "Detached HEAD": "A state in which HEAD points directly to a commit rather than a branch.",
        "Diff": "A line-by-line representation of changes between file states.",
        "Distributed version control": "A model in which each clone contains the project's complete history.",
        "Fetch": "The operation that downloads remote objects and references without merging them.",
        "Fork": "A GitHub-hosted copy of another user's repository under a different account.",
        "Git": "A distributed version control system for tracking changes to files.",
        "GitHub": "A hosted collaboration platform built around Git repositories.",
        "HEAD": "Git's reference to the commit or branch currently checked out.",
        "Issue": "A GitHub record used to discuss and track work, bugs, or proposals.",
        "Job": "A set of GitHub Actions steps executed by the same runner.",
        "Merge": "The operation that combines histories from two branches.",
        "Milestone": "A grouping of issues and pull requests toward a target outcome or date.",
        "Origin": "The conventional name for the primary remote created during cloning.",
        "Personal access token": "A revocable credential used in place of a password for supported operations.",
        "Project": "A GitHub planning view for organizing and tracking issues and pull requests.",
        "Pull": "A fetch followed by integration into the current branch.",
        "Pull request": "A GitHub proposal to review and merge changes from one branch into another.",
        "Push": "The operation that uploads local commits and updates remote references.",
        "Remote": "A named connection to another copy of a repository.",
        "Repository": "A project directory together with its Git objects, references, and configuration.",
        "Restore": "A Git command that restores working-tree or staged file content from another state.",
        "Runner": "A machine that executes jobs in a GitHub Actions workflow.",
        "Staging area": "The index that holds the exact content planned for the next commit.",
        "Tag": "A durable name for a specific commit, often used for releases.",
        "Workflow": "A YAML-defined automated process stored in `.github/workflows`.",
        "Working tree": "The files currently checked out for viewing and editing.",
    }
    titles = [
        "Introduction to Git and GitHub",
        "Setting Up Git and GitHub",
        "Creating the First Repository",
        "Essential Git Commands",
        "Branching and Merging",
        "Collaborating with Teams",
        "Managing Issues and Projects",
        "Repository and Workflow Best Practices",
        "GitHub Actions and Automation",
        "GitHub Pages and Static-Site Publishing",
        "Security and Advanced GitHub Features",
        "Contributing to Open Source Projects",
        "Troubleshooting and Recovery",
    ]
    outputs = [
        "Version-control concept map",
        "Verified Git identity and authentication",
        "Repository with initial commit",
        "Three-commit project history",
        "Merged feature branch and resolved conflict",
        "Reviewed pull request",
        "Tracked issue and project item",
        "Repository quality audit",
        "Passing validation workflow",
        "Published portfolio site",
        "Repository security review",
        "Contribution plan or documentation pull request",
        "Troubleshooting evidence log",
    ]
    roadmap = [
        {
            "unit": str(index),
            "title": title,
            "time": "3 hours" if index in {5, 6, 9, 10, 13} else "2 hours",
            "output": outputs[index - 1],
            "assessment": "Post-test and performance rubric",
        }
        for index, title in enumerate(titles, 1)
    ]
    return {"preface": preface, "glossary": glossary, "semester_roadmap": roadmap}
