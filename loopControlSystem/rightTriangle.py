# Reading a value from user
n = int(input())

# Looping for n times
for i in range(1,n+1):
    # Looping from 1 to i inclusive
    for j in range(1,i+1):
        # Printing value of j
        print(j,end="")
    # Looping from i-1 to 1 inclusive
    for j in range(i - 1, 0, -1):
        # Printing value of j
        print(j, end="")
    # Printing new line
    print()