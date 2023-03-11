import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    edge_cnts = [0] * N
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
        edge_cnts[u - 1] += 1
    is_visited = [False] * N

    def dfs(v, v_cnt):
        edge = edge_cnts[v]
        for u in graph[v]:
            if is_visited[u]:
                continue
            is_visited[u] = True
            e, vc = dfs(u, v_cnt + 1)
            edge += e
            v_cnt = vc
        return edge, v_cnt

    for u in range(N):
        if is_visited[u]:
            continue
        is_visited[u] = True
        e, v = dfs(u, 1)
        if e != v:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
