N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
C_dash = [B[C[i]-1] for i in range(N)]

Counter = [0]*(N+1)
for i in range(N):
    Counter[C_dash[i]-1]+=1

ans = 0
for i in range(N):
    ans += Counter[A[i]-1]
print(ans)