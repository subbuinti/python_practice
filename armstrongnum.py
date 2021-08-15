number = input()
length = len(number)
total = 0
for digit in number:
    total = total + (int(digit) ** length)
if total == int(number):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")