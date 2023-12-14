list1 = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
print("Let's loop the list items using for loop")
for i in list1:
    print(i)
print('')

print ('''Let's loop the list items using the index values.
We need to create a suitable iterable.
For that we will use range() and len()''')
print('')

list2 = ['1st', '2nd', '3rd', '4th', '5th']
for i in range(len(list2)):
    print(list2[i])

print('')
print("Using while loop to loop through the list items")
print('')
list3 = ['ek', 'do', 'teen', 'char', 'panch']
i = 0
while i < len(list3):
    print(list3[i])
    i += 1


