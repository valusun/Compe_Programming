from typing import NamedTuple


class Values(NamedTuple):
    min_cost: int
    max_souvenir: int


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [list(input()) for _ in range(N)]
    points = [[Values(N, 0)] * N for _ in range(N)]
    # 同一箇所の最短costを0にする
    for i in range(N):
        points[i][i] = Values(0, 0)
    # 直接つながっている箇所を(1, A[j])で埋める(A[i]は最後に足す)
    for i in range(N):
        for j in range(N):
            if S[i][j] == "Y":
                points[i][j] = Values(1, A[j])
    # ワーシャルフロイドで埋めていく
    for k in range(N):
        for i in range(N):
            for j in range(N):
                now_min_cost, now_max_souvenir = points[i][j]
                cost = points[i][k].min_cost + points[k][j].min_cost
                souvenir = points[i][k].max_souvenir + points[k][j].max_souvenir
                if cost < now_min_cost:
                    points[i][j] = Values(cost, souvenir)
                elif cost == now_min_cost and now_max_souvenir < souvenir:
                    points[i][j] = Values(now_min_cost, souvenir)

    Q = int(input())
    for _ in range(Q):
        u, v = map(int, input().split())
        if points[u - 1][v - 1].min_cost == N:
            print("Impossible")
            continue
        # TODO: ちょっと気持ち悪い書き方なので考える
        c, s = points[u - 1][v - 1]
        print(*(c, s + A[u - 1]))


if __name__ == "__main__":
    main()
