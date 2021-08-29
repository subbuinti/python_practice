a = int(input())
b = int(input())
c = int(input())
equ = ((a == b) and (a == c) and (c == a))
iso = ((a == b ) or (a == c) or (c == a) or (b ==c))
sca = ((a != b ) or (a != c) or (c != a) or (b != c))

if equ:
    print("Equilateral")
elif iso:
    print("Isosceles")
elif sca:
    print("Scalene")