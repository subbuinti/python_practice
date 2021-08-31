a = str(input())
b = str(input())
def SubstringFinder(a, b):
    answer = ""
    len1, len2 = len(a), len(b)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and a[i + j] == b[j]):
                match += b[j]
            else:
                if (len(match) > len(answer)): 
                    answer = match
                    match = ""
    if answer == "":
        return 'No overlapping'
    else:
        return answer

print(SubstringFinder(a, b))
