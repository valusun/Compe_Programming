def main():
    N, H, W = map(int, input().split())
    for i in range(N * H):
        for j in range(N * W):
            if ((i // H) + (j // W)) % 2:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    main()
