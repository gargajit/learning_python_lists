list1 = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
print("Let's loop the list items")
for i in list1:
    print(i)
print('')

print ('''Let's loop the list items using the index values.
We need to create a suitable iterable.''')
print('')

for i in range(len(list1)):
    print(list1[i])
