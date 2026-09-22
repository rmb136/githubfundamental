import unittest

from github_im.content.catalog import build_module
from github_im.validation import validate_module


class CompleteModuleTests(unittest.TestCase):
    def test_module_contains_all_units_and_back_matter(self):
        module = build_module()
        self.assertEqual([unit.number for unit in module.units], list(range(1, 14)))
        self.assertEqual(validate_module(module), [])
        self.assertEqual(
            set(module.rubrics), {"unit_performance", "pull_request", "capstone"}
        )
        self.assertGreaterEqual(len(module.glossary), 30)
        self.assertEqual(len(module.semester_roadmap), 13)

    def test_every_assessment_has_a_specific_answer(self):
        module = build_module()
        for unit in module.units:
            questions = unit.pretest + unit.self_test + unit.posttest
            with self.subTest(unit=unit.number):
                self.assertEqual(set(unit.answer_key), {q.id for q in questions})
                self.assertTrue(all(len(answer.split()) >= 3 for answer in unit.answer_key.values()))

    def test_capstone_integrates_setup_through_publishing(self):
        capstone = build_module().capstone
        combined = " ".join(capstone.instructions).lower()
        for artifact in (
            "readme",
            "issue",
            "feature branch",
            "pull request",
            "workflow",
            "github pages",
        ):
            self.assertIn(artifact, combined)


if __name__ == "__main__":
    unittest.main()
