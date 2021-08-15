number = int(input())
is_multiply_by_11 = ((number % 11) == 0)
is_multiple_times_by_11 =((number % 11)  == 1)
if is_multiply_by_11 or is_multiple_times_by_11:
    print("Special Eleven")
else:
    print("Normal Number")