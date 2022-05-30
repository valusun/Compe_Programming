def GetFirstCarriage(train, x):
    """先頭車両を取得する

    Args:
        train (list[list[int, int]]): 車両情報
        x (int): 車両
    """

    while train[x][0] != -1:
        x = train[x][0]
    return x


def main():
    N, Q = map(int, input().split())
    train = [[-1, -1] for _ in range(N)]
    for _ in range(Q):
        t, *a = map(int, input().split())
        x = a[0] - 1
        if t == 1:
            y = a[1] - 1
            train[x][1] = y
            train[y][0] = x
        elif t == 2:
            y = a[1] - 1
            train[x][1] = -1
            train[y][0] = -1
        else:
            ans = [GetFirstCarriage(train, x)]
            while train[ans[-1]][1] != -1:
                ans.append(train[ans[-1]][1])
                ans[-2] += 1
            ans[-1] += 1
            print(len(ans), *ans)


if __name__ == "__main__":
    main()
