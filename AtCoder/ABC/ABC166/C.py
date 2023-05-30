def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    ans = [True] * N
    for _ in range(M):
        a, b = map(int, input().split())
        if ans[a - 1]:
            ans[a - 1] = True if H[a - 1] > H[b - 1] else False
        if ans[b - 1]:
            ans[b - 1] = True if H[b - 1] > H[a - 1] else False
    print(sum(ans))


if __name__ == "__main__":
    main()
