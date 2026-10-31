import json

# Load the dataset
with open("data_full.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Get the training examples
training_data = data["train"]

# Collect all different intents
intents = set()

for example in training_data:
    intent = example[1]
    intents.add(intent)

# Display the report
print("\nCLINC150 INTENT REPORT")
print("======================")

print("Training examples:", len(training_data))
print("Number of different intents:", len(intents))

print("\nLIST OF INTENTS")
print("======================")

for intent in sorted(intents):
    print(intent)

print("\nINTENT INSPECTION COMPLETE!")