def main():
    sx, sy, tx, ty = map(int, input().split())
    dx, dy = tx - sx, ty - sy
    print("U" * dy, "R" * dx, "D" * dy, "L" * dx, sep="", end="")
    dx, dy = dx + 1, dy + 1
    print("L", "U" * dy, "R" * dx, "D", "R", "D" * dy, "L" * dx, "U", sep="")


if __name__ == "__main__":
    main()
