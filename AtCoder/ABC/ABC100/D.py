def main():
    N, M = map(int, input().split())
    cakes_params = [list(map(int, input().split())) for _ in range(N)]
    ans = -float("inf")

    for i in range(8):
        cakes = []
        for j in range(N):
            tmp = 0
            for k in range(3):
                if i & (1 << k):
                    tmp += cakes_params[j][k]
                else:
                    tmp -= cakes_params[j][k]
            cakes.append(tmp)
        cakes = sorted(cakes, reverse=True)
        ans = max(ans, sum(cakes[:M]))
    print(ans)


if __name__ == "__main__":
    main()
