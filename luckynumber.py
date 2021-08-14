a = int(input())
b = int(input())
any_num_6 = ((a==6) or (b==6))
sum_eqal_6 = ((a+b)==6)
diff_eqal_6 = ((a-b)==6) or ((b-a)==6)
sum_or_diff_eqal_6 = sum_eqal_6 or diff_eqal_6
if any_num_6 or sum_or_diff_eqal_6:
    print("Lucky")
else:
    print("Not Lucky")