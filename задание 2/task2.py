# задание 2
text = input("Введите текс: ")

text = text.lower()
text = text.replace(',', '').replace('.', '').replace('!', '')
words = text.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sortt = sorted(word_counts.items(), key = lambda x: x[1], reverse = True)

print('топ-5 самых частых слов')

for word, count in sortt[:5]:
    print(f"{word} : {count}")
