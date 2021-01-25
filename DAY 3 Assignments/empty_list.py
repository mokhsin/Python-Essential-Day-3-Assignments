list1 = [1, 2, [], 3, "Kenya", "India", '', [], 4, 5, [], 55]
for items in list1:
    if items == []:
        list1.remove(items)
print(list1)
