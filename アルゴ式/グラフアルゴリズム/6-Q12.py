from collections import deque


def main():
    def MemoTreeInfo(s):
        visited[s] = True
        Q = deque()
        Q.append(s)
        while Q:
            v = Q.popleft()
            for nv in Graph[v]:
                if visited[nv]:
                    continue
                visited[nv] = True
                children[v].append(nv)
                parent[nv] = v
                Q.append(nv)

    def GetMaximumStableSetPattern():
        children_cnt = [len(c) for c in children]
        leaf = [i for i, v in enumerate(children_cnt) if v == 0]
        Q = deque()
        for i in leaf:
            Q.append(i)
        while Q:
            v = Q.popleft()
            a1 = a2 = 1
            for nv in children[v]:
                a1 *= not_chosen_dp[nv]
                a1 %= MOD
                a2 *= chosen_dp[nv] + not_chosen_dp[nv]
                a2 %= MOD
            chosen_dp[v] = a1
            not_chosen_dp[v] = a2
            p = parent[v]
            children_cnt[p] -= 1
            if not children_cnt[p]:
                Q.append(p)

    N = int(input())
    Graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)
    MOD = 998244353
    visited = [False] * N
    children = [[] for _ in range(N)]
    parent = [-1] * N
    MemoTreeInfo(0)
    chosen_dp = [0] * N
    not_chosen_dp = [0] * N
    GetMaximumStableSetPattern()
    print((chosen_dp[0] + not_chosen_dp[0]) % MOD)


if __name__ == "__main__":
    main()
