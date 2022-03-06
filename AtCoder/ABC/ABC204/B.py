N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
    ans += max(0, A[i]-10)
print(ans)