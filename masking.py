word = input()
length_of_the_word = len(word)
number_of_character_to_mask = length_of_the_word - 2
masked_word = word[0] + "*" * number_of_character_to_mask +word[length_of_the_word-1]
print(masked_word)
