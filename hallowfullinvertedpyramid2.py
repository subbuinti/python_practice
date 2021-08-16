n = int(input())
for row in range(1, n+1):
    i=n -(row-1)
    left_space = " " * (row-1)
    if (i>2) and (i<n):
        hollow_space = "  " * (i-2)
        num = "1 " + hollow_space+ (str(i) + " ")
        print(left_space+ num)
    else:
        num =""
        for j in range(1, i+1):
            num = num + (str(j) + " ")
        print(left_space+ num)