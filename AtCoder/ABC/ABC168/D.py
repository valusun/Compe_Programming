from collections import deque


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    signposts = [-1] * N
    signposts[0] = 0
    Q = deque([0])
    while Q:
        v = Q.popleft()
        for u in graph[v]:
            if signposts[u] != -1:
                continue
            signposts[u] = v + 1
            Q.append(u)

    if -1 in signposts:
        print("No")
    else:
        print("Yes", *signposts[1:], sep="\n")


if __name__ == "__main__":
    main()
