def main():
    H, W = map(int, input().split())
    Field = [list(input()) for _ in range(H)]
    positions = []
    for i in range(H):
        for j in range(W):
            if Field[i][j] == "o":
                positions.append((i, j))
    a, b = positions[0]
    c, d = positions[1]
    print(abs(a - c) + abs(b - d))


if __name__ == "__main__":
    main()
