def main():
    N = int(input())
    X = list(map(int, input().split()))
    called = [False] * N
    for i, x in enumerate(X):
        if called[i]:
            continue
        called[x - 1] = True
    ans = [i + 1 for i, c in enumerate(called) if not c]
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
