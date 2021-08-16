sentence = input()

first_space_index = 0
for char in sentence:
    if char == " ":
        break
    first_space_index = first_space_index + 1
upper_case_word = sentence[:first_space_index].upper()
new_sentence = upper_case_word + sentence[first_space_index:]
print(new_sentence)