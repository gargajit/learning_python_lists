#Example 1
main_list = ['abc', 'pqr', 'xyz']
print("Example 1:")
print(main_list)
new_list = [x.upper() for x in main_list]   
print(new_list)

print("")

fruits = ['kiwi', 'strawberry', 'orange', 'banana', 'mango']
print("Example 2:")
print(fruits)
new_fruitlist = [x if x != "banana" else "orange" for x in fruits]
print(new_fruitlist)
