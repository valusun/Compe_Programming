def GetUnique(n):
    n.sort()
    if n[0] == n[1]:
        return n[2]
    return n[0]


def main():
    x, y = [], []
    for _ in range(3):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    print(GetUnique(x), GetUnique(y))


if __name__ == "__main__":
    main()
