N,K = map(int,input().split())
A = [sum(list(map(int,input().split()))) for _ in range(N)]
B = sorted(A, reverse=True)

Target = B[K-1]
for i in range(N):
    print(A[i]+300, Target)
    if A[i]+300 >= Target:
        print("Yes")
    else:
        print("No")