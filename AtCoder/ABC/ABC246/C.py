N, K, X = map(int, input().split())
A = sorted(list(map(int, input().split())))

for i in range(N):
    if A[i] // X <= K:
        K -= A[i] // X
        A[i] %= X
    else:
        A[i] -= K * X
        K = 0
        break

A.sort(reverse=True)
print(sum(A[K:]))
