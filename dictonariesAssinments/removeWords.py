def String(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1 

def remove(sentence, n):
    n_words = []
    words = sentence.split(" ")
    for word in words:
        if not len(word) == n:
            n_words.append(word)
            n_words.append(" ")
    return String(n_words)


a = str(input())
n = int(input())
print(remove(a, n))