thislist = ["banana", "Orange", "Kiwi", "cherry", "mango"]
print(thislist)
print("By default sort() is case-sensitive, resulting in all capital letters being sorted before lower letters ")

thislist.sort()
print("Case-sensitive:" , thislist)

thislist.sort(key = str.lower)        #to make case insensitive we used str.lower
print("Case-insensitive:", thislist)    
