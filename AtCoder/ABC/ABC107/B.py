def DeleteAllDotLine(field):
    tmp = []
    for f in field:
        if f.count(".") != len(f):
            tmp.append(f)
    return tmp


def Transpose(array):
    return list(list(f) for f in zip(*array))


def main():
    H, _ = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    field = DeleteAllDotLine(field)
    field = DeleteAllDotLine(Transpose(field))
    for f in Transpose(field):
        print(*f, sep="")


if __name__ == "__main__":
    main()
