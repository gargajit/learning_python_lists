main_list = ['pen', 'notebook', 'clothes', 'watch', 'cake', 'camera', 'football']
print(main_list)
new_list1 = []       #declaring the list
print("")
print("Without List Comprehension we use for loop")
for x in main_list:
    if 'c' in x:
        new_list1.append(x)

print(new_list1)
print("")
print("With List Comprehension we can do this in one line")
new_list2 = [x for x in main_list if 'c' in x]
print("new_list = [x for x in main_list if 'c' in x]")
print(new_list2)
