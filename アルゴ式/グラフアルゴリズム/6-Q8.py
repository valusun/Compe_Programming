from collections import deque


def main():
    def MemoTreeInfo(start):
        visited[start] = True
        parent[start] = start
        Q = deque()
        Q.append(start)
        while Q:
            v = Q.popleft()
            for nv in Graph[v]:
                if visited[nv]:
                    continue
                visited[nv] = True
                parent[nv] = v
                children[v].append(nv)
                Q.append(nv)

    def ChooseEdge():
        children_cnt = [len(c) for c in children]
        leaf = [i for i, v in enumerate(children_cnt) if v == 0]
        Q = deque()
        for v in leaf:
            Q.append(v)
        while Q:
            v = Q.popleft()
            p = parent[v]
            if p == v:
                continue
            if not (is_chosen[v] or is_chosen[p]):
                is_chosen[v] = is_chosen[p] = True
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
    parent = [-1] * N
    children = [[] for _ in range(N)]
    MemoTreeInfo(0)
    is_chosen = [False] * N
    ChooseEdge()
    print(is_chosen.count(True) // 2)


if __name__ == "__main__":
    main()
