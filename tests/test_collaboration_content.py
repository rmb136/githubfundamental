import unittest

from github_im.content.collaboration import build_collaboration_units
from github_im.validation import validate_unit


class CollaborationContentTests(unittest.TestCase):
    def test_units_five_through_nine_are_complete(self):
        units = build_collaboration_units()
        self.assertEqual([unit.number for unit in units], [5, 6, 7, 8, 9])
        for unit in units:
            with self.subTest(unit=unit.number):
                self.assertGreaterEqual(len(unit.discussion), 5)
                self.assertEqual(len(unit.posttest), 10)
                self.assertEqual(validate_unit(unit), [])

    def test_branching_and_collaboration_outputs_are_authentic(self):
        units = {unit.number: unit for unit in build_collaboration_units()}
        unit5_commands = "\n".join(command for command, _ in units[5].command_examples)
        self.assertIn("git switch -c feature/about-page", unit5_commands)
        self.assertIn("git merge feature/about-page", unit5_commands)
        self.assertIn("conflict", " ".join(units[5].activities[0].instructions).lower())
        self.assertIn("pull request", units[6].performance_task.evidence.lower())
        self.assertIn("issue", units[7].performance_task.evidence.lower())

    def test_best_practices_and_actions_include_safety(self):
        units = {unit.number: unit for unit in build_collaboration_units()}
        unit8_text = " ".join(units[8].discussion + [units[8].performance_task.safety_note]).lower()
        self.assertIn(".env", unit8_text)
        self.assertIn("revoke", unit8_text)
        workflow = "\n".join(command for command, _ in units[9].command_examples)
        self.assertIn(".github/workflows/validate.yml", workflow)
        self.assertIn("permissions:", workflow)
        self.assertIn("contents: read", workflow)
        self.assertIn("pull_request", workflow)


if __name__ == "__main__":
    unittest.main()
