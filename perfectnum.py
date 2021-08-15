number =int(input())
total = 0
for i in range(1, number):
    if (number % i ) ==0:
        total = total+ i
if total == number:
    print("Perfect Number")
else:
    print( "Not a Perfect Number")