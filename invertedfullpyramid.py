num_rows = int(input())
for i in range(num_rows):
    left_spaces = " " * i
    stars = "* " * (num_rows - i)
    print(left_spaces + stars)