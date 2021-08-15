time = int(input())
mng = ((time >= 4) and (time < 12))
aftn = ((time >= 12 ) and (time < 16))
evng = ((time >= 16) and (time < 20))
if mng:
    print("Good Morning")
elif aftn:
    print("Good Afternoon")
elif evng:
    print("Good Evening")
else:
    print("Good Night")