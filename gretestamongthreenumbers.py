first = int(input())
second = int(input())
third = int(input())
if first> second:
    greatest = first
else:
    greatest = second
if third > greatest:
    greatest = third
print(greatest)