def main():
    N, X, Y = map(int, input().split())

    level = [[0, 0] for _ in range(N)]
    level[0][0] = 1
    for n in range(N - 1):
        level[n][1] += level[n][0] * X
        level[n + 1][0] += level[n][0] + level[n][1]
        level[n + 1][1] += level[n][1] * Y

    print(level[-1][1])


if __name__ == "__main__":
    main()
