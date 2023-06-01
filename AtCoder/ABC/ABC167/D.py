def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [False] * N
    now, cnt = 0, 0
    while cnt < K and not visited[now]:
        visited[now] = True
        now = A[now] - 1
        cnt += 1
    if cnt == K:
        print(now + 1)
        exit()
    cycle = []
    visited = [False] * N
    while not visited[now]:
        cycle.append(now + 1)
        visited[now] = True
        now = A[now] - 1
    print(cycle[(K - cnt) % len(cycle)])


if __name__ == "__main__":
    main()
