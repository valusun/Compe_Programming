import sys
sys.setrecursionlimit(10**9)

N = int(input())
T = [0]*N
A = []
for i in range(N):
    t,k,*a = map(int,input().split())
    T[i] = t
    A.append(a)

Ans = 0
Check = [0]*N
def dfs(n):
    global Ans
    Check[n] = 1
    Ans += T[n]
    for i in A[n]:
        if Check[i-1]:
            continue
        dfs(i-1)

dfs(N-1)
print(Ans)