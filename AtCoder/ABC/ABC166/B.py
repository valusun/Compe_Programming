def main():
    N, K = map(int, input().split())
    ans = set(range(1, N + 1))
    for _ in range(K):
        _ = int(input())
        ans -= set(map(int, input().split()))
    print(len(ans))


if __name__ == "__main__":
    main()
