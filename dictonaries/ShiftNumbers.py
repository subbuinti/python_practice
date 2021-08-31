
# get the string from the user
inputString =input("");
digits=""
letters=""
symbols=""
# Looping through a string.
for letter in inputString:
    if (letter.isdigit()):
        digits+=letter
    elif (letter.isalpha()):
        letters+= letter
    else:
        symbols+= letter
# Display a new string.
print(letters+digits+symbols)