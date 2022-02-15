import sys
sys.setrecursionlimit(10**9)

N = int(input())
A = [list(map(int,input().split())) for _ in range(N*2-1)]

Ans = 0
def dfs(Pair, Used):
    global Ans

    # 点数計算
    if len(Pair) == N:
        res = 0
        for i in range(N):
            x,y = Pair[i][0], Pair[i][1]
            res ^= A[x][y-x-1]
        Ans = max(Ans, res)

    else:
        # ペア1人目を決める
        for i in range(2*N):
            if Used[i]: continue
            Used[i] = 1
            first = i
            break

        # 2人目を決める
        for j in range(first+1, 2*N):
            if Used[j]: continue
            Pair.append((first, j))
            Used[j] = 1
            dfs(Pair, Used)
            Used[j] = 0
            Pair.pop()

        Used[first] = 0

dfs(list(), [0]*(2*N))
print(Ans)