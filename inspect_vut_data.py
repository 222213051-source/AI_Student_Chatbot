import json

with open("student_support_data/vut_student_questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

print("\nVUT STUDENT SUPPORT DATASET")
print("===========================")

print("Total questions:", len(questions))

print("\nQUESTIONS BY INTENT")
print("===================")

intents = set()

for question in questions:
    intents.add(question["intent"])

for intent in sorted(intents):
    count = sum(1 for q in questions if q["intent"] == intent)
    print(intent, "=", count, "questions")

print("\nDATASET INSPECTION COMPLETE!")