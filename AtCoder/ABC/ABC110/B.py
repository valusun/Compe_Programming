def main():
    N, M, X, Y = map(int, input().split())
    A = max(list(map(int, input().split())))
    B = min(list(map(int, input().split())))
    for i in range(X + 1, Y + 1):
        if A < i <= B:
            print("No War")
            break
    else:
        print("War")


if __name__ == "__main__":
    main()
