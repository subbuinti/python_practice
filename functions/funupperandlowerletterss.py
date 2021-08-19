def get_lower_and_upper_case_letters(word):
    # Complete this function
    uppercase_letters = ""
    lowercase_letters = ""
    for letter in word:
        if letter.upper() == letter:
            uppercase_letters += letter
        else:
            lowercase_letters += letter
    print(uppercase_letters)
    print(lowercase_letters)
    

word = input()
# Call the get_lower_and_upper_case_letters function
get_lower_and_upper_case_letters(word)
