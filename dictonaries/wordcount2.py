words = {}
for str in input().split():
    word = ("".join([ c if c.isalnum() else "" for c in str ]))
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

for word in sorted(words):
    print(word, ": ", words[word], sep='')