N,M = map(int,input().split())
A = list(input().split())
B = list(input().split())

for i in range(M):
    if B[i] in A:
        A.remove(B[i])
    else:
        print("No")
        break
else:
    print("Yes")

