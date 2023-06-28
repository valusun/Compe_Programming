def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while X * A < Y and (X * A) - X < B:
        ans += 1
        X *= A
    ans = ans + (Y - X) // B
    if (Y - X) % B == 0:
        ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
