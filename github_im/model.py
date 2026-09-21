from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


QuestionKind = Literal["multiple_choice", "short_answer", "performance"]


@dataclass
class Question:
    id: str
    prompt: str
    kind: QuestionKind
    answer: str
    choices: tuple[str, ...] = ()
    objective_ids: tuple[str, ...] = ()


@dataclass
class Activity:
    id: str
    title: str
    instructions: list[str]
    evidence: str
    objective_ids: tuple[str, ...]
    safety_note: str = ""


@dataclass
class Unit:
    number: int
    title: str
    time_allotment: str
    overview: str
    rationale: str
    objectives: list[str]
    objective_ids: list[str]
    learner_instructions: list[str]
    materials: list[str]
    pretest: list[Question]
    discussion: list[str]
    command_examples: list[tuple[str, str]]
    activities: list[Activity]
    self_test: list[Question]
    performance_task: Activity
    posttest: list[Question]
    supplementary_readings: list[str]
    references: list[str]
    figure_key: str
    answer_key: dict[str, str] = field(default_factory=dict)


@dataclass
class Module:
    title: str
    audience: str
    preface: list[str]
    glossary: dict[str, str]
    semester_roadmap: list[dict[str, str]]
    units: list[Unit]
    capstone: Activity
    rubrics: dict[str, list[tuple[str, str]]]
    references: list[str]

