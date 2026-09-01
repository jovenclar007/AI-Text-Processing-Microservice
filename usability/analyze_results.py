"""Calculate simple usability-testing results from usability_test_form.csv.

Enter task results as Pass or Fail and overall rating from 1 to 5.
Run:
    python usability/analyze_results.py
"""

import csv
from pathlib import Path

FILE = Path(__file__).with_name("usability_test_form.csv")
TASKS = ["task_health", "task_analyze", "task_batch", "task_translate"]


def main():
    with FILE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    completed = 0
    task_passes = {task: 0 for task in TASKS}
    ratings = []

    for row in rows:
        if row["all_tasks_completed"].strip().lower() == "yes":
            completed += 1

        for task in TASKS:
            if row[task].strip().lower() == "pass":
                task_passes[task] += 1

        try:
            rating = float(row["overall_rating_1_to_5"])
            if 1 <= rating <= 5:
                ratings.append(rating)
        except ValueError:
            pass

    total = len(rows)
    print("Usability Testing Results")
    print("=" * 28)
    print(f"Participants: {total}")

    if total:
        print(f"All-task completion rate: {completed / total * 100:.1f}%")
        for task, passed in task_passes.items():
            print(f"{task}: {passed / total * 100:.1f}% pass rate")
    else:
        print("No participant data entered yet.")

    if ratings:
        print(f"Average overall rating: {sum(ratings) / len(ratings):.2f}/5")
    else:
        print("Average overall rating: no ratings entered")


if __name__ == "__main__":
    main()
