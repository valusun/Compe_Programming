def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AC = set()

    def SortPointAndIdx(point):
        ret = []
        for i, p in enumerate(point):
            ret.append([p, -(i + 1)])
        return sorted(ret, reverse=True)

    def SortPointsAndIdx(point_a, point_b):
        ret = []
        for i in range(len(point_a)):
            ret.append([point_a[i] + point_b[i], -(i + 1)])
        return sorted(ret, reverse=True)

    x_cnt = 0
    for _, i in SortPointAndIdx(A):
        if x_cnt == X:
            break
        if -i not in AC:
            AC.add(-i)
            x_cnt += 1

    y_cnt = 0
    for _, i in SortPointAndIdx(B):
        if y_cnt == Y:
            break
        if -i not in AC:
            AC.add(-i)
            y_cnt += 1

    z_cnt = 0
    for _, i in SortPointsAndIdx(A, B):
        if z_cnt == Z:
            break
        if -i not in AC:
            AC.add(-i)
            z_cnt += 1

    print(*sorted(list(AC)), sep="\n")


if __name__ == "__main__":
    main()
