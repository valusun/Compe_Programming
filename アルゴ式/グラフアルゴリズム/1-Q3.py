def main():
    N, M = map(int, input().split())
    friends = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    print(*sorted(max(friends, key=lambda x: len(x))))


if __name__ == "__main__":
    main()
