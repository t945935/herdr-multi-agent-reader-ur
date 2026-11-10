"""ابواب 2/4/5/6 کا مشترکہ contract؛ ranking میں unrounded total استعمال ہوتا ہے۔"""

from collections.abc import Mapping
from math import isfinite

SUBJECTS = frozenset({"اردو", "انگریزی", "ریاضی"})


def validate_scores(scores):
    if not isinstance(scores, Mapping) or set(scores) != SUBJECTS:
        raise ValueError("scores میں صرف اردو، انگریزی اور ریاضی ہونے چاہییں")
    for value in scores.values():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("نمبر int یا float ہوں؛ bool قابلِ قبول نہیں")
        if not isfinite(value) or not 0 <= value <= 100:
            raise ValueError("نمبر محدود ہوں اور 0 سے 100 کے درمیان ہوں")
    return scores


def calculate_total(scores):
    return sum(validate_scores(scores).values())


def calculate_average(scores):
    return calculate_total(scores) / 3


def get_grade(average):
    if isinstance(average, bool) or not isinstance(average, (int, float)):
        raise ValueError("اوسط عددی ہونی چاہیے")
    if not isfinite(average) or not 0 <= average <= 100:
        raise ValueError("اوسط 0 سے 100 کے درمیان ہونی چاہیے")
    return "کامیاب" if average >= 60 else "ناکام"


def rank_students(students):
    if not isinstance(students, list):
        raise ValueError("students کی قدر فہرست ہونی چاہیے")
    rows = []
    for student in students:
        if not isinstance(student, Mapping):
            raise ValueError("ہر طالب علم object ہونا چاہیے")
        name = student.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("طالب علم کا نام درکار ہے")
        total = calculate_total(student.get("scores"))
        average = total / 3
        rows.append({"name": name.strip(), "scores": dict(student["scores"]),
                     "total": total, "average": average, "grade": get_grade(average)})
    rows.sort(key=lambda row: row["total"], reverse=True)
    previous = None
    rank = 0
    for index, row in enumerate(rows, 1):
        if previous is None or row["total"] != previous:
            rank = index
        previous = row["total"]
        row["rank"] = rank
    return rows
