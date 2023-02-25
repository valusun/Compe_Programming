def main():
    X, K = map(int, input().split())
    for i in range(K):
        X //= 10**i
        amount = X % 10
        if amount >= 5:
            X += 10 - amount
        else:
            X -= amount
        X *= 10**i
    print(X)


if __name__ == "__main__":
    main()
