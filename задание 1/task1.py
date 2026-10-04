# задание 1.1
# students - список, внутри списка лежат словари, внутри словарей списки
# с оценками
students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]}, # элемент 0, каждый эл-нт словарь
    {"name": "Bob", "grades": [4, 4, 4, 5]}, # элемент 1, лежит по 2 key в каждом
    {"name": "Charlie", "grades": [5, 5, 5, 5]}, # элемент 2
]
#переменная student - это словарь
# можно достават из него значения по ключам
averages = {
    student.get("name", "ключ не найден") : sum(student.get("grades")) / len(student.get("grades"))
    for student in students
}
print("Средние оценки", averages)

# заданеи 1.2
best_score = -1
best_student = None
for name, score in averages.items():
    if score > best_score:
        best_score = score
        best_student = name

print(f"Лучший студент : {best_student} с оценкой {best_score}")
