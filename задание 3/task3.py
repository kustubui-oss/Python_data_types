# задание 3.1
list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]
common = []
uniq = []

for x in list1:
    for y in list2:
        if x == y:
            common.append(x)
# задание 3.2

for x in list1:
    if x not in list2:
        uniq.append(x)

for x in list2:
    if x not in list1:
        uniq.append(x)

print('общие элементы:', *common)
print('уникальные элементы:', *uniq)