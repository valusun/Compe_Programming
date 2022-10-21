def main():
    N, M = map(int, input().split())
    followers = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        followers[a].append(b)
    for f in followers:
        print(*sorted(f))


if __name__ == "__main__":
    main()
