'''Author:Anugrah Chandran
Date:22-11-24
Description:'Program to construct patterns of stars (*), using a nested for loop.'''
size= int(input("Enter the size of the star pattern: "))
print("Increasing Triangle: ")
for i in range(1,size+1):
    for j in range(i):
        print("*",end="\t")
    print()

size= int(input("Enter the size of the star pattern: "))
print("Decreasing  Triangle: ")
for i in range(size,0,-1):
    for j in range(i):
        print("*",end="\t")
    print()

size= int(input("Enter the size of the star pattern: "))
print("Hill Triangle: ")
for i in range(1,size+1):
    for j in range(size-i):
        print(" ",end="\t")
    for k in range(2*i-1):
        print("*",end="\t")
    print()

size= int(input("Enter the size of the star pattern: "))
print("Reverse Hill Pattern: ")
for i in range(size,0,-1):
    for j in range(size-i):
        print(" ",end="\t")
    for k in range(2*i-1):
        print("*",end="\t")
    print()