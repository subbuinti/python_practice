Abhinav_choice = str(input ())
Anjali_choice = str (input ())
if Abhinav_choice == Anjali_choice:
    print ("Tie")
elif Abhinav_choice == "Rock":
    if Anjali_choice == "Paper":
        print ("Anjali Wins")
    else:
         print ("Abhinav Wins")
elif Abhinav_choice == "Paper":
    if Anjali_choice == "Rock":
         print ("Abhinav Wins")
    else:
         print ("Anjali Wins")
elif Anjali_choice == "Rock":
     print ("Anjali Wins")
else:
     print ("Abhinav Wins")