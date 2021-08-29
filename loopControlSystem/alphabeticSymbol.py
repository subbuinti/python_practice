import string

# Get user input
N = int(input())

for i in range(N):

   slice = string.ascii_uppercase[0: i + 1]
  
   print(" ".join(slice))