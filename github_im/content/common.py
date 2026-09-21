from __future__ import annotations

from github_im.model import Activity, Question, Unit


def _questions(
    unit_number: int,
    prefix: str,
    items: list[tuple[str, str]],
    objective_ids: tuple[str, ...],
) -> list[Question]:
    return [
        Question(
            id=f"u{unit_number}-{prefix}-{index}",
            prompt=prompt,
            kind="short_answer",
            answer=answer,
            objective_ids=(objective_ids[(index - 1) % len(objective_ids)],),
        )
        for index, (prompt, answer) in enumerate(items, 1)
    ]


def make_unit(
    *,
    number: int,
    title: str,
    time_allotment: str,
    overview: str,
    rationale: str,
    objectives: list[str],
    learner_instructions: list[str],
    materials: list[str],
    discussion: list[str],
    command_examples: list[tuple[str, str]],
    activity_title: str,
    activity_steps: list[str],
    evidence: str,
    safety_note: str,
    assessment_items: list[tuple[str, str]],
    supplementary_readings: list[str],
    references: list[str],
    figure_key: str,
) -> Unit:
    if len(assessment_items) != 10:
        raise ValueError("Each unit requires exactly ten assessment items")
    objective_ids = [f"u{number}-o{index}" for index in range(1, len(objectives) + 1)]
    objective_tuple = tuple(objective_ids)
    pretest = _questions(number, "pre", assessment_items[:5], objective_tuple)
    self_test = _questions(number, "self", assessment_items[5:], objective_tuple)
    posttest = _questions(number, "post", assessment_items, objective_tuple)
    activity = Activity(
        id=f"u{number}-guided",
        title=activity_title,
        instructions=activity_steps,
        evidence=evidence,
        objective_ids=objective_tuple,
        safety_note=safety_note,
    )
    performance = Activity(
        id=f"u{number}-performance",
        title=f"Performance Task: {activity_title}",
        instructions=activity_steps,
        evidence=evidence,
        objective_ids=objective_tuple,
        safety_note=safety_note,
    )
    questions = pretest + self_test + posttest
    return Unit(
        number=number,
        title=title,
        time_allotment=time_allotment,
        overview=overview,
        rationale=rationale,
        objectives=objectives,
        objective_ids=objective_ids,
        learner_instructions=learner_instructions,
        materials=materials,
        pretest=pretest,
        discussion=discussion,
        command_examples=command_examples,
        activities=[activity],
        self_test=self_test,
        performance_task=performance,
        posttest=posttest,
        supplementary_readings=supplementary_readings,
        references=references,
        figure_key=figure_key,
        answer_key={question.id: question.answer for question in questions},
    )


GIT_REFERENCE = "Git. (2026). Git reference. https://git-scm.com/docs"
GITHUB_REFERENCE = "GitHub. (2026). GitHub Docs. https://docs.github.com/"

