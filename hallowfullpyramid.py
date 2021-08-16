n = int(input())
for i in range(1, n+1):
    left_space = " " * (n-i)
    if (i >2) and (i < n):
        hollow_space = "  " * (i-2)
        stars = "* " + hollow_space + "* "
        print(left_space+stars)
    else:
        stars = "* " * i
        print(left_space + stars)