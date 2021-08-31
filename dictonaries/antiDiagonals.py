def antidiagonals(M, N, matrix):
    antidiagonals = [[] for _ in range(M+N-1)]
    for i in range(M*N):
        adindex = (i // N) + (i % N)
        antidiagonals[adindex].append(matrix[i])
    for d in antidiagonals:
        print(*d)

# Driver code
M, N = list(map(int, input().split()))
A = []
for i in range(1, M+1):
    A += map(int, input().split())

antidiagonals(M, N, A)

