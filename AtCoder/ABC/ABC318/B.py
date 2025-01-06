def main():
    N = int(input())
    S = list(map(int, input().split()) for _ in range(N))

    sheet = set()
    for a, b, c, d in S:
        for i in range(a, b):
            for j in range(c, d):
                sheet.add((i, j))
    print(len(sheet))


if __name__ == "__main__":
    main()
