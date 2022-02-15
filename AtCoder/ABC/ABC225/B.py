N = int(input())
A = [0]*N
for i in range(N-1):
    a,b = map(int,input().split())
    A[a-1]+=1
    A[b-1]+=1

for i in range(N):
    if A[i] == N-1:
        print("Yes")
        break
else:
    print("No")