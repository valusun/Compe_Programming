N,X = map(int,input().split())
A = []
for i in range(N):
    L,*a = map(int,input().split())
    A.append(sorted(a))

Ans = 0
def dfs(cnt, res):
    global Ans

    # N個の袋からボールを取り出したか
    if cnt == N:
        if res == X:
            Ans+=1
        return

    # cnt個目の袋からボールを取り出す
    for i in A[cnt]:
        if res*i > X:
            return
        dfs(cnt+1, res*i)

dfs(0, 1)
print(Ans)
