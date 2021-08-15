month = int(input())
winter = (((month==12) or (month ==11)) or (month ==1))
spring = ((month == 2) or (month ==3))
summer = (((month ==4) or (month ==5)) or (month ==6))
rainy = ((month ==7) or (month == 8))
if winter:
    print("Winter")
elif spring:
    print("Spring")
elif summer:
    print("Summer")
elif rainy:
    print("Rainy")
else:
    print("Autumn")