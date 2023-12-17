main_list = ['apple pie', 'banana chips', 'orange juice', 'banana shake', 'apple custard', 'vanilla-apple cake', 'banana peanut butter sandwich']
print(main_list)
new_list1 = []       #declaring the list
print("")
print("Without List Comprehension we use for loop")
for x in main_list:
    if 'apple' in x:
        new_list1.append(x)

print(new_list1)
print("")
print("With List Comprehension we can do this in one line")
new_list2 = [x for x in main_list if 'apple' in x]
print("new_list = [x for x in main_list if 'c' in x]")
print(new_list2)

print("")

print("All items without 'apple'")
new_list3 = [x for x in main_list if "apple" not in x]
print(new_list3)
