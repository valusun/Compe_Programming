def main():
    A, B, C, X = [int(input()) for _ in range(4)]
    ans = 0
    for i in range(A + 1):
        for j in range(B + 1):
            now = X - i * 500 - j * 100
            if now >= 0 and now % 50 == 0 and now // 50 <= C:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
