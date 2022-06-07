def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    grid = [["."] * (S - R + 1) for _ in range(Q - P + 1)]
    drawing_start = max(P - A, R - B)
    drawing_end = min(Q - A, S - B)
    for d in range(drawing_start, drawing_end + 1):
        grid[A + d - P][B + d - R] = "#"
    drawing_start = max(P - A, B - S)
    drawing_end = min(Q - A, B - R)
    for d in range(drawing_start, drawing_end + 1):
        grid[A + d - P][B - d - R] = "#"
    for g in grid:
        print(*g, sep="")


if __name__ == "__main__":
    main()
