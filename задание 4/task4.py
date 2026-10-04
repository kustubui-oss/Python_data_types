items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("tomato", "vegetable"),
    ("milk", "dairy")
]
diction = {}

for value, key in items:
    if key not in diction:
        diction[key] = [value]
    else:
        diction[key].append(value)

for x, y in diction.items():
    print(f"{x} : {y}")