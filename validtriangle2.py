a = int(input())
b = int(input())
c = int(input())
con_1 = ((a+b)>c)
con_2 = ((b+c)>a)
con_3 = ((c+a)>b)
if (con_1 and con_2) and con_3:
    print("It's a Triangle")
else:
    print("It's not a Triangle")