import unittest

from github_im.content.publishing import build_publishing_units
from github_im.validation import validate_unit


class AdvancedContentTests(unittest.TestCase):
    def test_units_ten_through_thirteen_are_complete(self):
        units = build_publishing_units()
        self.assertEqual([unit.number for unit in units], [10, 11, 12, 13])
        for unit in units:
            with self.subTest(unit=unit.number):
                self.assertGreaterEqual(len(unit.discussion), 5)
                self.assertEqual(len(unit.pretest), 5)
                self.assertEqual(len(unit.posttest), 10)
                self.assertEqual(validate_unit(unit), [])

    def test_publishing_and_security_are_safe_for_students(self):
        units = {unit.number: unit for unit in build_publishing_units()}
        pages_text = " ".join(units[10].discussion + units[10].activities[0].instructions).lower()
        self.assertIn("index.html", pages_text)
        self.assertIn("privacy", pages_text)
        security_text = " ".join(units[11].discussion).lower()
        for concept in ("least privilege", "two-factor", "dependabot", "code scanning"):
            self.assertIn(concept, security_text)

    def test_recovery_unit_places_dangerous_commands_behind_safety_guidance(self):
        unit = build_publishing_units()[3]
        text = " ".join(unit.discussion).lower()
        commands = "\n".join(command for command, _ in unit.command_examples).lower()
        safety = unit.performance_task.safety_note.lower()
        self.assertIn("git reflog", commands)
        self.assertIn("git reset --hard", commands)
        self.assertIn("revoke", text)
        self.assertIn("reset --hard", safety)
        self.assertIn("instructor", safety)


if __name__ == "__main__":
    unittest.main()
