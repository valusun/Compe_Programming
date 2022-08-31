def main():
    N = int(input())
    X = list(map(int, input().split()))
    sorted_X = sorted(X)
    tgt = sorted_X[N // 2]
    for i in X:
        idx = N // 2 if i < tgt else N // 2 - 1
        print(sorted_X[idx])


if __name__ == "__main__":
    main()
