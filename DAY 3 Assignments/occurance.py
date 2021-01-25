from collections import Counter
word = 'book'
w = Counter(word)
for i, n in w.items():
    print(f'{i} has appeared {n} times')
