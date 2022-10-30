from collections import deque


def main():
    def MemoTreeInfo(s):
        Q = deque()
        Q.append(s)
        visited[s] = True
        while Q:
            v = Q.popleft()
            for u in Graph[v]:
                if visited[u]:
                    continue
                visited[u] = True
                children[v].append(u)
                parent[u] = v
                Q.append(u)

    def ChooseMinimumVertexCover():
        children_cnt = [len(c) for c in children]
        leaf = [i for i, v in enumerate(children_cnt) if v == 0]
        Q = deque()
        for v in leaf:
            Q.append(v)
        while Q:
            v = Q.popleft()
            for u in children[v]:
                if not is_chosen[u]:
                    is_chosen[v] = True
                    break
            p = parent[v]
            if p == -1:
                continue
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
    is_chosen = [False] * N
    ChooseMinimumVertexCover()
    print(is_chosen.count(True))


if __name__ == "__main__":
    main()
