import unittest

from github_im.content.foundations import build_foundation_units
from github_im.content.front_matter import build_front_matter
from github_im.validation import validate_unit


class FoundationContentTests(unittest.TestCase):
    def test_front_matter_is_complete(self):
        front = build_front_matter()
        self.assertGreaterEqual(len(front["preface"]), 2)
        self.assertGreaterEqual(len(front["glossary"]), 30)
        self.assertEqual(len(front["semester_roadmap"]), 13)

    def test_foundation_units_meet_contract(self):
        units = build_foundation_units()
        self.assertEqual([unit.number for unit in units], [1, 2, 3, 4])
        self.assertEqual(
            [unit.title for unit in units],
            [
                "Introduction to Git and GitHub",
                "Setting Up Git and GitHub",
                "Creating the First Repository",
                "Essential Git Commands",
            ],
        )
        for unit in units:
            with self.subTest(unit=unit.number):
                self.assertGreaterEqual(len(unit.discussion), 5)
                self.assertEqual(len(unit.pretest), 5)
                self.assertGreaterEqual(len(unit.self_test), 5)
                self.assertEqual(len(unit.posttest), 10)
                self.assertEqual(validate_unit(unit), [])

    def test_foundation_commands_cover_beginner_workflow(self):
        units = {unit.number: unit for unit in build_foundation_units()}
        commands = {
            number: "\n".join(command for command, _ in unit.command_examples)
            for number, unit in units.items()
        }
        self.assertIn("git --version", commands[2])
        self.assertIn("git config --global user.name", commands[2])
        for command in ("git init", "git clone", "git remote -v", "git push -u origin main"):
            self.assertIn(command, commands[3])
        for command in ("git status", "git add", "git commit", "git log", "git diff"):
            self.assertIn(command, commands[4])

    def test_identity_unit_protects_credentials(self):
        unit = build_foundation_units()[1]
        combined = " ".join(
            [unit.performance_task.safety_note]
            + [activity.safety_note for activity in unit.activities]
        ).lower()
        self.assertIn("never submit", combined)
        self.assertIn("private key", combined)
        self.assertIn("personal access token", combined)


if __name__ == "__main__":
    unittest.main()
