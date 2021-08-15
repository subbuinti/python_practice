A = int(input())
B = int(input())
a_power_b = (A ** B)
b_power_a = (B ** A)
if a_power_b > b_power_a:
    print(a_power_b)
else:
    print(b_power_a)