def main():
    _ = int(input())
    S = input()
    visited = set()
    visited.add((0, 0))
    nx, ny = 0, 0
    for s in S:
        if s == "R":
            nx, ny = nx + 1, ny
        elif s == "L":
            nx, ny = nx - 1, ny
        elif s == "U":
            nx, ny = nx, ny + 1
        else:
            nx, ny = nx, ny - 1
        if (nx, ny) in visited:
            print("Yes")
            break
        visited.add((nx, ny))
    else:
        print("No")


if __name__ == "__main__":
    main()
