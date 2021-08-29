x = int(input())
import calendar

if  (x <= 12):
    print(calendar.month_name[x])

else:
    print("Invalid Month Number")
