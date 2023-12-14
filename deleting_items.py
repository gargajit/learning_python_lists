list1 = ['a', 'b', 'c', 'd', 'b', 'e']
print(list1)

print("Let's remove items using del keyword")
del list1[-2:]
print(list1)

print("Let's delete the entire list")
del list1
print("Now if you print(list1) it will show error list1 not defined")
