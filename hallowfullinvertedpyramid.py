n =int(input())
for row in range(1, n+1):
    i = n - (row-1)
    left_space = " " * (n-i)
    if (i>2) and (i <n):
        hollow_spaces = "  " * (i-2)
        stars = "* " + hollow_spaces + "* "
        print(left_space + stars)
    else:
        stars = "* " * i