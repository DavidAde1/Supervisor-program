import sys

#using the sys library to check if a name is in the list created below
names = ["Bill", "David", "Paul", "Patrick", "George", "Giannis", "praise"]

name = input("Name: ")

if name in names:
    print("Found")
    sys.exit(0)

print("Not Found")
sys.exit(1)