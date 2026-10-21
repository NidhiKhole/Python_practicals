# Linear Search using Strings
names = ["Amit", "Rahul", "Priya", "Sneha", "Neha"]

search = input("Enter name to search: ")
found = False

for i in range(len(names)):
    if names[i] == search:
        print("Name found at position", i + 1)
        found = True
        break

if not found:
    print("Name not found")