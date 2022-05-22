def main():
    from heapq import heappush, heappop

    n, m = map(int, input().split())
    ans = []

    graph = [[] for _ in range(n)]

    for i in range(m):
        u, v, c = map(int, input().split())

        graph[u - 1].append((v - 1, c, i + 1))  # u->vの辺
        graph[v - 1].append((u - 1, c, i + 1))  # v->uの辺

    # プリム法
    # 頂点がマークされているか確認する配列
    marked = [False for _ in range(n)]

    # マークされている頂点数を数える
    marked_cnt = 0

    # はじめに0頂点をマーク
    marked[0] = True
    marked_cnt += 1

    # heap
    q = []

    # 頂点0に隣接する辺を保存
    for j, c, i in graph[0]:
        heappush(q, (c, j, i))

    total = 0

    # すべての頂点をマークするまでwhileループ
    while marked_cnt < n:
        # 最小の重みの辺をheapで取り出す
        c, i, k = heappop(q)

        # マークされているならスキップ
        if marked[i]:
            continue

        # 頂点をマーク
        marked[i] = True
        marked_cnt += 1

        total += c
        tmp = c
        ans.append(k)

        # 頂点iに隣接する辺を保存
        for j, c, k in graph[i]:
            # マークされていればスキップ
            if marked[j]:
                continue
            heappush(q, (c + tmp, j, k))

    print(*ans)


if __name__ == "__main__":
    main()
