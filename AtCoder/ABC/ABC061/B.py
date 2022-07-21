def main():
    N, M = map(int, input().split())
    edges = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a - 1] += 1
        edges[b - 1] += 1
    print(*edges, sep="\n")


if __name__ == "__main__":
    main()
