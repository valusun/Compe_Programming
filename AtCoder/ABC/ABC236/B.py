N = int(input())
A = list(map(int,input().split()))

A.sort()
for i in range(3, 4*N-1, 4):
    if A[i] != i//4+1:
        print(i//4+1)
        break
else:
    print(N)