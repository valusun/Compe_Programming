def ToMaximum(sequence: list[str]) -> int:
    """並び替えて出来る最大値を返す

    Args:
        sequence (list[str]): 数列

    Returns:
        int: 最大値
    """

    return int("".join(sorted(sequence, reverse=True)))


def main():
    N = input()
    ans = 0
    for i in range(1, 2 ** len(N) - 1):
        x, y = [], []
        for j, v in enumerate(N):
            if i & (1 << j):
                x.append(v)
            else:
                y.append(v)
        ans = max(ans, ToMaximum(x) * ToMaximum(y))
    print(ans)


if __name__ == "__main__":
    main()
