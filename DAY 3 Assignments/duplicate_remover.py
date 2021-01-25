str1 = input("Enter a string with duplicate words: ")
list1 = []
for words in str1.split():
    if words not in list1:
        list1.append(words)
print(f'Duplicate free is {list1}')
