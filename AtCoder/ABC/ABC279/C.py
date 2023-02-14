def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    T = [list(input()) for _ in range(H)]
    St = sorted(list(zip(*S)))
    Tt = sorted(list(zip(*T)))
    print("Yes" if St == Tt else "No")


if __name__ == "__main__":
    main()
