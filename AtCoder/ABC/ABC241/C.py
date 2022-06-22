def CheckTate(F, h, w):
    dot = 0
    for i in range(6):
        if F[h + i][w] == ".":
            dot += 1
            if dot == 3:
                return False
    return True


def CheckYoko(F, h, w):
    dot = 0
    for i in range(6):
        if F[h][w + i] == ".":
            dot += 1
            if dot == 3:
                return False
    return True


def CheckLowerRight(F, h, w):
    dot = 0
    for i in range(6):
        if F[h + i][w + i] == ".":
            dot += 1
            if dot == 3:
                return False
    return True


def CheckLowerLeft(F, h, w):
    dot = 0
    for i in range(6):
        if F[h + i][w - i] == ".":
            dot += 1
            if dot == 3:
                return False
    return True


def main():
    N = int(input())
    Field = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i + 6 <= N:
                # 縦
                if CheckTate(Field, i, j):
                    print("Yes")
                    exit()
                # 右下斜め
                if j + 6 <= N and CheckLowerRight(Field, i, j):
                    print("Yes")
                    exit()
                # 左下斜め
                if j - 5 >= 0 and CheckLowerLeft(Field, i, j):
                    print("Yes")
                    exit()
            # 横
            if j + 6 <= N and CheckYoko(Field, i, j):
                print("Yes")
                exit()
    print("No")


if __name__ == "__main__":
    main()
