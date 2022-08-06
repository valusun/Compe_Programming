def main():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if i in edges[j] and j in edges[k] and k in edges[i]:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
