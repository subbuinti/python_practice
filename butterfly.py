n = int(input())
for i in range(1, n+1):
    stars = "* " * i
    middle_space = "  " * (2*(n-i))
    print(stars + middle_space + stars)
for i in range(n):
    stars = "* " * (n-i)
    middle_space = "  " * (2*i)
    print(stars + middle_space + stars)