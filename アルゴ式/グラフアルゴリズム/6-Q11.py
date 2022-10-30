from collections import deque


def main():
    def MemoTreeInfo(s):
        visited[s] = True
        Q = deque()
        Q.append(s)
        while Q:
            v = Q.popleft()
            for u in Graph[v]:
                if visited[u]:
                    continue
                visited[u] = True
                parent[u] = v
                children[v].append(u)
                Q.append(u)

    def GetMaximumStableSet():
        children_cnt = [len(c) for c in children]
        leaf = [i for i, v in enumerate(children_cnt) if v == 0]
        Q = deque()
        for i in leaf:
            Q.append(i)
        while Q:
            v = Q.popleft()
            a1 = Weight[v]
            a2 = 0
            for u in children[v]:
                a1 += not_chosen_dp[u]
                a2 += max(chosen_dp[u], not_chosen_dp[u])
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
    Weight = list(map(int, input().split()))
    visited = [False] * N
    children = [[] for _ in range(N)]
    parent = [-1] * N
    MemoTreeInfo(0)
    chosen_dp = [0] * N
    not_chosen_dp = [0] * N
    GetMaximumStableSet()
    print(max(chosen_dp[0], not_chosen_dp[0]))


if __name__ == "__main__":
    main()
