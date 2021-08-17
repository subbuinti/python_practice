full_string = input()
subseq = input()
subseq_index = 0
subseq_len = len(subseq)

for char in full_string:
    if char == subseq[subseq_index]:
        subseq_index += 1
        if subseq_index == subseq_len:
            break
if subseq_index == subseq_len:
    print("Yes")
else:
    print("No")