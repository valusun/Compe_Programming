def main():
    A, B, K = map(int, input().split())
    for a in range(A, min(B, A + K - 1) + 1):
        print(a)
    for b in range(max(B - K + 1, A + K), B + 1):
        print(b)


if __name__ == "__main__":
    main()
