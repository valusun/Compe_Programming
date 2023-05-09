from typing import NamedTuple


class Magic(NamedTuple):
    damage: int
    mp: int


def main():
    H, N = map(int, input().split())
    magics = [Magic(*map(int, input().split())) for _ in range(N)]
    INF = 10**9
    dp = [INF] * (H + 1)
    dp[0] = 0
    for i in range(H):
        for m in magics:
            nxt = min(H, i + m.damage)
            dp[nxt] = min(dp[nxt], dp[i] + m.mp)
    print(dp[H])


if __name__ == "__main__":
    main()
