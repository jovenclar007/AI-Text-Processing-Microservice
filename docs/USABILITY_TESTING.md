# Usability Testing

## Purpose

The usability test checks whether a new user can understand and use the main API functions without technical assistance.

This is a small academic usability test for the MSIT 132 project. It is not a formal human-subject research study.

## Participants

Use 3–5 classmates or other available users who have basic familiarity with a web browser or Postman.
Do not collect names, email addresses, or other personal information. Use participant IDs such as P01, P02, and P03.

## Test Tasks

Ask each participant to perform these tasks in Postman:

| Task | User Goal | Success Condition |
|---|---|---|
| 1. Health | Check whether the service is running | Receives HTTP 200 and `status: healthy` |
| 2. Analyze | Analyze a short sentence | Receives word, character, and sentence counts |
| 3. Batch Analyze | Analyze several texts | Receives results for every text |
| 4. Translate | Translate a short phrase | Receives a translated text |

## Procedure

1. Start the microservice.
2. Give the participant the four task descriptions above.
3. Do not explain which endpoint to use unless the participant is completely stuck.
4. Record Pass or Fail for each task.
5. Ask the participant to give an overall rating from 1 (very difficult) to 5 (very easy).
6. Record short comments about anything confusing.
7. Do not record names or private information.

## Data Collection

Use `usability_test_form.csv` to record the results.

For each task, enter `Pass` or `Fail`.
For `all_tasks_completed`, enter `Yes` or `No`.
For the rating, enter a number from 1 to 5.

## Calculate Results

After entering the participant data, run:

```powershell
python usability\analyze_results.py
```

The script calculates:

- number of participants
- overall task-completion rate
- pass rate for each task
- average usability rating

## Results Table for the Final Report

After the test is completed, copy the script output into this section or into the final presentation.

| Measure | Result |
|---|---|
| Participants | Enter actual number |
| All-task completion rate | Enter actual result |
| Health pass rate | Enter actual result |
| Analyze pass rate | Enter actual result |
| Batch pass rate | Enter actual result |
| Translate pass rate | Enter actual result |
| Average rating | Enter actual result / 5 |

**Important:** Do not invent usability results. The values above should be replaced with the results from the actual participants.

## Defense Explanation

> "I performed a small usability test with classmates. Each participant completed four simple API tasks: health check, text analysis, batch analysis, and translation. I recorded whether each task was completed and asked for an overall 1-to-5 ease-of-use rating. I used a small Python script to calculate the completion and pass rates."
