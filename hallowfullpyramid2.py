n = int(input())
for i in range(1, n+1):
    left_spaces = " " * (n-i)
    if (i>2) and (i<n):
        hollow_space = " " * (2*(i-2))
        num = "1 " + hollow_space + (str(i) + " ")
        print(left_spaces + num)
    else:
        num = ""
        for j in range(1, i+1):
            num = num + (str(j) + " ")
        print(left_spaces + num)