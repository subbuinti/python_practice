rows = int(input())
columns = int(input())
number_pattern = ""
for k in range(1, columns+1):
    number_pattern = number_pattern + (str(k)+ " ")
for i in range(rows):
    print(number_pattern)