list1 = ['a', 'b', 'c', 'b', 'd', 'e', 'remove']
print(list1)
print("Let's pop out the duplicate b at the wrong alphabetical order")

#pop() method with a index will remove that item.
list1.pop(3)
print(list1)

#pop() method without an index will remove the last item.
list1.pop()
print(list1)
