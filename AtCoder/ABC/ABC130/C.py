def main():
    W, H, x, y = map(int, input().split())
    if x + x == W and y + y == H:
        print(H * W / 2, 1)
    else:
        print(H * W / 2, 0)


if __name__ == "__main__":
    main()
