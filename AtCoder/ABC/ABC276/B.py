def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a - 1].append(b)
        Graph[b - 1].append(a)
    for g in Graph:
        print(len(g), *list(sorted(g)))


if __name__ == "__main__":
    main()
