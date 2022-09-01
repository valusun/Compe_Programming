def main():
    A, B, C, X, Y = map(int, input().split())
    if C * 2 > A + B:
        print(X * A + Y * B)
    else:
        Z = min(X, Y)
        ans = Z * 2 * C
        if X != Z:
            ans += (X - Z) * min(A, C * 2)
        if Y != Z:
            ans += (Y - Z) * min(B, C * 2)
        print(ans)


if __name__ == "__main__":
    main()
