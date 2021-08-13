word = input()
n =  int(input())
length = len(word)
start_index =(length-3)
sliced_word = word[start_index:]
message = sliced_word* n


print(message)