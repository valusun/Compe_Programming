def CheckResult(x: str, y: str) -> int:
    """勝敗を判定する

    Args:
        x (str): xが出した手
        y (str): yが出した手

    Returns:
        int: xが負けたら1,勝ったら0,引き分けは-1
    """

    if x == y:
        return -1
    elif (x, y) in (("G", "C"), ("C", "P"), ("P", "G")):
        return 1
    else:
        return 0


def main():
    N, M = map(int, input().split())
    humans_hands = [list(input()) for _ in range(N * 2)]
    humans_points = [[0, i] for i in range(N * 2)]
    for i in range(M):
        for j in range(N):
            x, y = (
                humans_points[j * 2][1],
                humans_points[j * 2 + 1][1],
            )
            x_hand, y_hand = humans_hands[x][i], humans_hands[y][i]
            result = CheckResult(x_hand, y_hand)
            if result == 1:
                humans_points[j * 2][0] -= 1
            elif result == 0:
                humans_points[j * 2 + 1][0] -= 1
        humans_points.sort()
    for _, i in humans_points:
        print(i + 1)


if __name__ == "__main__":
    main()
