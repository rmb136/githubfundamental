from __future__ import annotations

import re

from .model import Module, Unit


GENERIC_ANSWERS = (
    "see the unit content",
    "see chapter content",
    "answers may vary",
)


def _all_text(unit: Unit) -> str:
    parts = [unit.overview, unit.rationale, *unit.discussion]
    parts.extend(command for command, _ in unit.command_examples)
    parts.extend(explanation for _, explanation in unit.command_examples)
    parts.extend(activity.safety_note for activity in unit.activities)
    parts.append(unit.performance_task.safety_note)
    return "\n".join(parts)


def validate_unit(unit: Unit) -> list[str]:
    errors: list[str] = []
    required = (
        "title",
        "time_allotment",
        "overview",
        "rationale",
        "objectives",
        "objective_ids",
        "learner_instructions",
        "materials",
        "pretest",
        "discussion",
        "activities",
        "self_test",
        "posttest",
        "supplementary_readings",
        "references",
        "figure_key",
        "answer_key",
    )
    for name in required:
        if not getattr(unit, name):
            errors.append(f"{name} is required")

    if len(unit.objectives) != len(unit.objective_ids):
        errors.append("objectives and objective_ids must have equal length")
    if unit.pretest and len(unit.pretest) != 5:
        errors.append("pretest must contain exactly 5 questions")
    if unit.self_test and len(unit.self_test) < 5:
        errors.append("self_test must contain at least 5 questions")
    if unit.posttest and len(unit.posttest) != 10:
        errors.append("posttest must contain exactly 10 questions")

    questions = [*unit.pretest, *unit.self_test, *unit.posttest]
    ids = [question.id for question in questions]
    if len(ids) != len(set(ids)):
        errors.append("question IDs must be unique within a unit")

    activity_objectives = {
        objective_id
        for activity in [*unit.activities, unit.performance_task]
        for objective_id in activity.objective_ids
    }
    assessment_objectives = {
        objective_id for question in questions for objective_id in question.objective_ids
    }
    for objective_id in unit.objective_ids:
        if objective_id not in activity_objectives:
            errors.append(f"objective {objective_id} has no activity mapping")
        if objective_id not in assessment_objectives:
            errors.append(f"objective {objective_id} has no assessment mapping")

    for question in questions:
        if not question.answer.strip():
            errors.append(f"{question.id} has no answer")
        answer = unit.answer_key.get(question.id, "").strip()
        if not answer:
            errors.append(f"{question.id} is missing from answer_key")
        elif any(marker in answer.lower() for marker in GENERIC_ANSWERS):
            errors.append(f"{question.id} uses a generic answer")

    text = _all_text(unit)
    lower = text.lower()
    if "-----begin" in lower and "private key-----" in lower:
        errors.append("content appears to contain a private key")
    if re.search(r"(?:ghp|github_pat)_[a-z0-9_]{12,}", lower):
        errors.append("content appears to contain an access token")
    destructive = ("git reset --hard", "git push --force", "git push -f")
    if any(command in lower for command in destructive):
        safety = " ".join(
            [activity.safety_note for activity in unit.activities]
            + [unit.performance_task.safety_note]
        ).lower()
        mentions_risk = any(
            phrase in safety
            for phrase in ("reset --hard", "force push", "history rewrite")
        )
        states_protection = any(
            word in safety for word in ("backup", "instructor", "practice", "safe")
        )
        if not (mentions_risk and states_protection):
            errors.append("unsafe command lacks a safety note")
    return errors


def validate_module(module: Module) -> list[str]:
    errors: list[str] = []
    numbers = [unit.number for unit in module.units]
    if numbers != list(range(1, 14)):
        errors.append("module must contain units 1 through 13 exactly once")
    figure_keys = [unit.figure_key for unit in module.units]
    if len(figure_keys) != len(set(figure_keys)):
        errors.append("module figure keys must be unique")
    if not module.preface:
        errors.append("module preface is required")
    if not module.glossary:
        errors.append("module glossary is required")
    roadmap_units = {str(row.get("unit", "")) for row in module.semester_roadmap}
    expected_units = {str(number) for number in range(1, 14)}
    if roadmap_units != expected_units:
        errors.append("semester roadmap must include units 1 through 13")
    if not module.capstone or not module.capstone.instructions:
        errors.append("module capstone is required")
    if not module.rubrics:
        errors.append("module rubrics are required")
    if not module.references:
        errors.append("module references are required")
    for unit in module.units:
        errors.extend(f"Unit {unit.number}: {error}" for error in validate_unit(unit))
    return errors
