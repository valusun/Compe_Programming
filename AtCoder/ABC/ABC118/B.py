def main():
    N, _ = map(int, input().split())
    K = [list(map(int, input().split()))[1:] for _ in range(N)]
    ans = set(K[0])
    for k in K[1:]:
        ans &= set(k)
    print(len(ans))


if __name__ == "__main__":
    main()
