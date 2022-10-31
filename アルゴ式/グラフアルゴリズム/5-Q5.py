from collections import deque


def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)
    Color = ["."] * N

    def bfs(q: deque):
        while q:
            v, c = q.popleft()
            Color[v] = c
            nc = "W" if c == "B" else "B"
            for nv in Graph[v]:
                if Color[nv] == ".":
                    q.append((nv, nc))
                elif Color[nv] == nc:
                    continue
                else:
                    print("No")
                    exit()

    Q = deque()
    for i in range(N):
        if Color[i] != ".":
            continue
        Q.append((i, "B"))
        bfs(Q)
    print("Yes")


if __name__ == "__main__":
    main()
