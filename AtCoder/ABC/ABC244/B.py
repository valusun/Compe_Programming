def main():
    _ = int(input())
    T = input()
    x, y = 0, 0
    direction = 0
    for s in T:
        if s == "S":
            if direction == 0:
                x += 1
            if direction == 1:
                y -= 1
            if direction == 2:
                x -= 1
            if direction == 3:
                y += 1
        else:
            direction = (direction + 1) % 4
    print(x, y)


if __name__ == "__main__":
    main()
