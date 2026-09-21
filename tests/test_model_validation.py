from dataclasses import replace
import unittest

from github_im.model import Activity, Module, Question, Unit
from github_im.validation import validate_module, validate_unit


def make_questions(prefix: str, count: int, objective_ids=("o1",)):
    return [
        Question(
            id=f"{prefix}-{index}",
            prompt=f"Question {index}",
            kind="short_answer",
            answer=f"Specific answer {index}",
            objective_ids=objective_ids,
        )
        for index in range(1, count + 1)
    ]


def make_unit():
    objectives = ["Explain version control", "Create a repository", "Work safely"]
    objective_ids = ["o1", "o2", "o3"]
    pretest = make_questions("pre", 5, tuple(objective_ids))
    self_test = make_questions("self", 5, tuple(objective_ids))
    posttest = make_questions("post", 10, tuple(objective_ids))
    activity = Activity(
        id="activity-1",
        title="Create a safe repository",
        instructions=["Create a folder.", "Initialize the repository."],
        evidence="A repository with one commit",
        objective_ids=tuple(objective_ids),
        safety_note="Use only the practice repository.",
    )
    answer_key = {
        question.id: question.answer for question in pretest + self_test + posttest
    }
    return Unit(
        number=1,
        title="Introduction to Git and GitHub",
        time_allotment="2 hours",
        overview="A practical introduction to version control.",
        rationale="Version history supports safe, accountable collaboration.",
        objectives=objectives,
        objective_ids=objective_ids,
        learner_instructions=["Use the practice folder only."],
        materials=["Computer", "Git"],
        pretest=pretest,
        discussion=["Git records snapshots of project files."],
        command_examples=[("git status", "Inspect repository state")],
        activities=[activity],
        self_test=self_test,
        performance_task=activity,
        posttest=posttest,
        supplementary_readings=["Git reference"],
        references=["Git. (2026). Git reference."],
        figure_key="unit-01-version-control-flow",
        answer_key=answer_key,
    )


class ModelValidationTests(unittest.TestCase):
    def setUp(self):
        self.unit = make_unit()

    def test_complete_unit_is_valid(self):
        self.assertEqual(validate_unit(self.unit), [])

    def test_rejects_missing_required_sections(self):
        for field_name in (
            "objectives",
            "pretest",
            "activities",
            "self_test",
            "posttest",
            "references",
            "answer_key",
        ):
            with self.subTest(field_name=field_name):
                unit = make_unit()
                setattr(unit, field_name, {} if field_name == "answer_key" else [])
                self.assertTrue(
                    any(field_name in error for error in validate_unit(unit))
                )

    def test_rejects_unmapped_objective(self):
        self.unit.objectives.append("Configure a remote safely")
        self.unit.objective_ids.append("o4")
        self.assertIn(
            "objective o4 has no activity mapping", validate_unit(self.unit)
        )

    def test_rejects_generic_answer(self):
        self.unit.answer_key["post-1"] = "See the unit content."
        self.assertIn("post-1 uses a generic answer", validate_unit(self.unit))

    def test_rejects_unqualified_destructive_command(self):
        self.unit.discussion.append("Run git reset --hard HEAD~1.")
        self.assertIn(
            "unsafe command lacks a safety note", validate_unit(self.unit)
        )

    def test_requires_thirteen_unique_units(self):
        units = [
            replace(self.unit, number=index, figure_key=f"figure-{index}")
            for index in range(1, 13)
        ]
        module = Module(
            title="GitHub Fundamentals",
            audience="Beginner BSIT students",
            preface=["Welcome."],
            glossary={"Git": "A distributed version control system."},
            semester_roadmap=[
                {"unit": str(index), "title": f"Unit {index}"}
                for index in range(1, 13)
            ],
            units=units,
            capstone=self.unit.performance_task,
            rubrics={"capstone": [("Correctness", "Accurate work")]},
            references=["Git. (2026). Documentation."],
        )
        self.assertIn(
            "module must contain units 1 through 13 exactly once",
            validate_module(module),
        )


if __name__ == "__main__":
    unittest.main()
