# Python 3 program to print a hallow diamond pattern given N number of rows
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
             'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
# Diamond array
diamond = []

rows = -1
# Prompt user to enter number of rows
while rows < 1 or rows > 26:
    rows = int(input())
for i in range(0, rows):
    # Add letters to the diamond
    diamond.append("")
    for j in range(0, rows - i):
        diamond[i] += " "
    diamond[i] += alphabets[i];
    if alphabets[i] != 'A':
        # Put spaces between letters
        for j in range(0, 2 * i - 1):
            diamond[i] += " "
        diamond[i] += alphabets[i]
    # Print the first part of the diamond
    print(diamond[i])
# Print the second part of the diamond
for i in reversed(range(0, rows - 1)):
    print(diamond[i])