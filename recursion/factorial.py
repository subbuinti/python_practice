def compute_factorial(n):
    # Complete this recursive function
    if n <= 0: #base case
        return 1
    else:
        return n * compute_factorial(n-1)  #recursion
    

num = int(input())
# Call the compute_factorial function
result = compute_factorial(num)
print(result)
