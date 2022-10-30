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
                children[v].append(u)
                parent[u] = v
                Q.append(u)

    def GetMinimumEdgeCover():
        nonlocal covered_edge_cnt
        children_cnt = [len(c) for c in children]
        leaf = [i for i, v in enumerate(children_cnt) if v == 0]
        Q = deque()
        for i in leaf:
            Q.append(i)
        while Q:
            v = Q.popleft()
            p = parent[v]
            if not is_covered[v]:
                is_covered[v] = is_covered[p] = True
                covered_edge_cnt += 1
            children_cnt[p] -= 1
            if not children_cnt[p]:
                Q.append(p)

    N = int(input())
    Graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)
    visited = [False] * N
    children = [[] for _ in range(N)]
    parent = [-1] * N
    MemoTreeInfo(0)
    is_covered = [False] * N
    covered_edge_cnt = 0
    GetMinimumEdgeCover()
    print(covered_edge_cnt)


if __name__ == "__main__":
    main()
