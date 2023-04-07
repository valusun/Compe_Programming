def main():
    K, X = map(int, input().split())
    min_x, max_x = X - K + 1, X + K - 1
    print(" ".join([str(k) for k in range(min_x, max_x + 1)]))


if __name__ == "__main__":
    main()
