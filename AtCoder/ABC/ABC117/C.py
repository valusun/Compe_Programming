def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))
    cost = sorted([X[i] - X[i - 1] for i in range(1, M)])
    print(sum(cost[: M - N]) if M - N >= 0 else 0)


if __name__ == "__main__":
    main()
