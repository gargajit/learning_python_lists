names = []

n = int(input("How many names do you want to enter? "))

for _ in range(n):
    names.append(input("Enter Name: "))

for name in sorted(names):
    print(f"Hello, {name}")
