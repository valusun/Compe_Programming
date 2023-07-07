def main():

    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    B = [list(input()) for _ in range(H)]
    for s in range(H):
        for t in range(W):
            f = True
            for i in range(H):
                for j in range(W):
                    if A[(i - s + H) % H][(j - t + W) % W] != B[i][j]:
                        f = False
            if f:
                print("Yes")
                exit()
    print("No")


if __name__ == "__main__":
    main()
