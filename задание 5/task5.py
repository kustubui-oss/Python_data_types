data = [
    {"student": "Alice", "subject": "Math", "grade": 5},
    {"student": "Bob", "subject": "Math", "grade": 4},
    {"student": "Alice", "subject": "History", "grade": 3},
    {"student": "Bob", "subject": "History", "grade": 5},
]
result = {}

for x in data:
    subject = x["subject"]
    student = x["student"]
    grade = x["grade"]

    if subject not in result:
        result[subject] = {}
    
    result[subject][student] = grade

print(result)