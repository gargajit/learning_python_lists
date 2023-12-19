import random

#List Comprehension and random range
new_list = [random.randrange(15,35) for x in range(10) if x % 2 == 0]
print(new_list)

new_list2 = [x for x in new_list if x % 2 == 0]
print(new_list2)
