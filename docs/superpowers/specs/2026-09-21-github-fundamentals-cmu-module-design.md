# GitHub Fundamentals CMU Module Design

## Purpose

Rebuild the existing GitHub Fundamentals instructional material as a publication-ready Central Mindanao University module for BSIT students who have no prior Git experience. The module will support a full semester through thirteen sequential units and will remain editable in Word while also producing a distribution-ready PDF.

## Success Criteria

- The document follows the CMU module outline and physical-format requirements supplied in the `guidelines` folder.
- All thirteen units teach a coherent beginner progression from version-control concepts to GitHub collaboration, automation, publishing, and troubleshooting.
- Every unit contains aligned behavioral objectives, instruction, guided practice, assessment, and references.
- Placeholder assessments and generic answer-key entries are completely replaced.
- Commands and GitHub procedures are checked against current official Git and GitHub documentation.
- The editable DOCX and final PDF render cleanly, consistently, and accessibly.
- The module includes a coherent set of original instructional images that clarify workflows, processes, examples, and abstract concepts.
- The generator can reproduce the deliverables without downloading dependencies or modifying the user's environment.

## Audience and Instructional Context

The primary audience is BSIT students with no previous Git experience. The material assumes basic familiarity with files, folders, a web browser, and text editing, but it does not assume prior command-line or software-development workflow knowledge. The instructor may deliver approximately one unit per week over a semester.

## Required CMU Format

The module will use:

- A4 portrait pages.
- Arial 11-point body text.
- Single line spacing.
- A 1-inch top margin.
- A 1-inch bottom margin.
- A 1.5-inch left margin.
- A 1-inch right margin.

The content structure will follow the CMU module outline:

1. Preliminary pages.
2. Overview for each learning unit.
3. Introduction or rationale.
4. Behavioral learning objectives.
5. Instructions to the learner.
6. Pre-test.
7. Learning activities integrating suitable pedagogy and media.
8. Concepts and discussion.
9. Self-test.
10. Post-test.
11. Notes and suggested supplementary readings.
12. References in APA format.

## Document Architecture

### Preliminary Pages

The front matter will contain:

- A formal title page.
- A preface explaining the module's scope, audience, and intended use.
- A table of contents with page references.
- A list of figures and a list of tables when applicable.
- A glossary of essential Git and GitHub terms.
- A semester roadmap that identifies each unit's suggested time, practical output, and assessment evidence.

### Learning Units

The module will preserve the existing thirteen-topic sequence:

1. Introduction to Git and GitHub.
2. Setting Up Git and GitHub.
3. Creating the First Repository.
4. Essential Git Commands.
5. Branching and Merging.
6. Collaborating with Teams.
7. Managing Issues and Projects.
8. Repository and Workflow Best Practices.
9. GitHub Actions and Automation.
10. GitHub Pages and Static-Site Publishing.
11. Security and Advanced GitHub Features.
12. Contributing to Open Source Projects.
13. Troubleshooting and Recovery.

Every unit will contain:

- Unit number, title, and suggested time allotment.
- A concise overview and rationale.
- Three to five observable behavioral objectives.
- Prerequisites, materials, and learner instructions.
- A short diagnostic pre-test.
- Concepts and discussion written from first principles.
- Accurate command examples using a consistent sample repository.
- At least one topic-specific workflow figure, table, or annotated example when it materially improves understanding.
- A guided hands-on activity with expected evidence of completion.
- A self-test with immediate feedback or an answer path.
- A practical performance task.
- A post-test aligned to the unit objectives.
- Notes, safety cautions, and suggested supplementary readings.
- Unit references in APA format.

### Back Matter

The final section will include:

- A beginner capstone project that integrates repository setup, branching, pull requests, issue tracking, automation, and publishing.
- Analytic rubrics for unit performance tasks and the capstone.
- Complete answer keys for pre-tests, self-tests, and post-tests.
- A concise Git command and workflow cheat sheet.
- Consolidated references in APA format.
- An About the Author page. Because author details have not been supplied, this page will use a neutral, clearly identified author-information section that can be completed without altering the module body; it will not invent biographical claims.

## Learning Design

Each unit will use the same learning cycle:

1. Diagnose prior knowledge with a short pre-test.
2. Introduce the workflow in plain language and with a focused visual where useful.
3. Model the workflow using the semester-long sample repository.
4. Guide the student through a hands-on activity.
5. Check conceptual understanding through a self-test and a troubleshooting scenario.
6. Require an authentic GitHub artifact or observable action as the performance output.
7. Measure attainment using an objective-aligned post-test.

The instructional voice will be direct, supportive, and technically precise. New terminology will be defined before use. Commands will be explained in terms of their effect on the working tree, staging area, local repository, and remote repository.

## Assessment Model

Assessment will emphasize authentic performance. Unit outputs may include a configured Git identity, a repository and commit history, a feature branch, a resolved merge conflict, a reviewed pull request, a populated issue board, a valid workflow file, or a published GitHub Pages site.

Each behavioral objective will map to at least one learning activity and one assessment item. Answer keys will provide specific model answers or observable completion criteria rather than generic references back to the chapter. Practical tasks will use concise analytic rubrics with criteria for correctness, process, documentation, and safe practice.

Potentially destructive or history-rewriting operations will be taught only in controlled recovery contexts. Safer commands and reversible workflows will appear first. Force-push, hard reset, secret handling, and authentication topics will include explicit cautions and recovery guidance.

## Technical Content and Sources

Technical procedures will be based primarily on current official sources, including Git documentation and GitHub Docs. The module will prefer contemporary commands such as `git switch` and `git restore` while also explaining common legacy equivalents when students are likely to encounter them. GitHub interface instructions will describe stable navigation concepts and avoid fragile pixel-specific wording where possible.

Examples will use a consistent fictional student project so that skills accumulate across units. Credentials, personal access tokens, private keys, and real secrets will never appear in examples. Screenshots will be used only when they add durable instructional value; conceptual diagrams and annotated command output will be preferred when the GitHub interface is likely to change.

## Instructional Visual Strategy

The implementation will create a coordinated set of original raster illustrations for the module using the built-in image-generation workflow. The selected images will be copied into the workspace and referenced by the reproducible document generator. Images will use a consistent academic flat-illustration style, a restrained blue and neutral palette, strong contrast, generous whitespace, and landscape compositions that reproduce clearly on A4 pages.

At minimum, the visual set will include one substantive image for each unit:

1. The relationship among a working directory, staging area, local repository, and GitHub remote.
2. Git installation, identity configuration, and secure authentication choices.
3. The lifecycle of creating, cloning, editing, committing, and pushing a repository.
4. The flow and effect of essential Git commands.
5. Branch creation, parallel work, merging, and conflict resolution.
6. A team collaboration cycle from branch or fork through pull-request review and merge.
7. The relationship among issues, labels, assignees, milestones, and a project board.
8. A healthy repository showing documentation, ignore rules, small commits, and protected collaboration practices.
9. A GitHub Actions continuous-integration pipeline from event trigger through test result.
10. The GitHub Pages publishing path from repository content to a public static site.
11. Layered repository security using least privilege, secret protection, dependency review, and code scanning.
12. The open-source contribution process from project discovery through accepted pull request.
13. A troubleshooting and recovery decision path for common beginner problems.

Generated illustrations will avoid logos presented as official branding, decorative stock imagery, watermarks, illegible interface mockups, and unnecessary embedded prose. Where exact wording or command syntax is essential, the generator will add deterministic labels, arrows, captions, or annotated command output around the generated visual so technical accuracy does not depend on text rendered inside an AI-generated image.

Each final image will be inspected for conceptual accuracy, visual consistency, text accuracy when text is unavoidable, and suitability for print. Images will be regenerated or corrected when they introduce misleading relationships, malformed text, irrelevant objects, or unclear sequencing. Every inserted image will receive a numbered caption, a source note identifying it as an original instructional illustration, and meaningful alternative text.

## Document Design

The document will use a restrained academic design appropriate for university publication. Titles and headings will be black, with hierarchy established through size, weight, spacing, and numbering. Body text will remain readable at the required Arial 11-point size. Command examples will use a compatible monospaced font and sufficient spacing without reducing legibility.

Tables will be used for comparative or repeated information such as command references, semester mapping, assessment rubrics, and troubleshooting matrices. Figures will be topic-specific, numbered, captioned, and supplied with alternative text. Page breaks will keep headings, captions, figures, and short assessments together where practical.

## Deliverables

The implementation will produce:

- `GitHub_Fundamentals_CMU_Module.docx` as the editable master.
- `GitHub_Fundamentals_CMU_Module.pdf` as the distribution copy.
- A complete instructor answer key, included in the module's back matter rather than maintained as an incomplete standalone text file.
- A workspace `figures/cmu-module` asset set containing the selected instructional illustrations used by the module.
- An updated deterministic Python generator that reproduces the module and its figures.

Existing files will be preserved. Final deliverables will use stable names rather than timestamped filenames.

## Verification

Verification will cover content, structure, and rendering:

- Compare the module against every item in the supplied CMU module outline and physical-format guideline.
- Confirm that all thirteen units include every required section.
- Audit the objective-activity-assessment mapping.
- Search for placeholders, generic questions, incomplete answers, and unsupported claims.
- Validate code blocks and command sequences for internal consistency.
- Check headings, table structure, figure captions, image alternative text, page numbering, and navigation.
- Inspect every generated image for conceptual accuracy, consistent style, print legibility, and absence of malformed or misleading text.
- Render the DOCX to page images and inspect every page for clipping, overlap, missing glyphs, broken tables, misplaced headers or footers, and awkward page breaks.
- Produce the PDF from the verified DOCX and compare its page count and visible content with the approved render.

If the packaged DOCX renderer is unavailable, use the bundled document runtime and an available office converter without modifying the user's installed applications. Do not claim visual verification until every final page has been inspected.

## Out of Scope

- Filling or signing the CMU application and endorsement forms on the author's behalf.
- Inventing the author's biography, institutional position, course code, enrollment numbers, or publication approvals.
- Creating or accessing real student GitHub accounts.
- Publishing the module or its sample repository to GitHub.
