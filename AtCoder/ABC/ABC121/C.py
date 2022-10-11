def main():
    N, M = map(int, input().split())
    drinks = [list(map(int, input().split())) for _ in range(N)]
    drinks.sort()

    cost, bought = 0, 0
    i = 0
    while bought < M:
        cost += min(M - bought, drinks[i][1]) * drinks[i][0]
        bought += min(M - bought, drinks[i][1])
        i += 1
    print(cost)


if __name__ == "__main__":
    main()
