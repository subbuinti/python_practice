attendance = input()
medical_reason = input()
lenght = len(attendance)
attendance = attendance[:(lenght-1)]
attendance = int(attendance)
if attendance >= 75:
    print("Allowed to write exam")
elif attendance <75 and medical_reason =="Y":
    print("Allowed to write exam")
elif attendance < 75 and medical_reason =="N":
    print("Cannot write exam")