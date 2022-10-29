from collections import deque


def main():
    def MemoTreeInfo():
        """ノードの子や親をメモする"""
        Q = deque()
        Q.append(0)
        visited[0] = True
        parent[0] = 0
        while Q:
            v = Q.popleft()
            for u in Graph[v]:
                if visited[u]:
                    continue
                visited[u] = True
                children[v].append(u)
                parent[u] = v
                Q.append(u)

    def GetMaximumStableSet():
        """最大安定集合に属する頂点を選ぶ"""
        Q = deque()
        children_cnt = [len(c) for c in children]
        for i, v in enumerate(children_cnt):
            if v == 0:
                Q.append(i)
        while Q:
            v = Q.popleft()
            is_chose = False
            for u in children[v]:
                is_chose |= is_chosen[u]  # 1つでも選ばれていたらTrueにする
            is_chosen[v] = not is_chose
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
    parent = [-1] * N
    children = [[] for _ in range(N)]
    visited = [False] * N
    MemoTreeInfo()
    is_chosen = [False] * N
    GetMaximumStableSet()
    print(is_chosen.count(True))


if __name__ == "__main__":
    main()
