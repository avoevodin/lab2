# Compiling the sieve of eratosthenes

N = 8
A = [True] * N
A[0] = A[1] = True

for k in range(2, N):
    if A[k]:
        for m in range(2*k, N, k):
            A[m] = False

for k in range(N):
    print(k, '-', "simple" if A[k] else "composite")
