def main():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = 0
    squares = [0] * 4
    for a in A:
        squares[0] += 1
        for i in range(3, -1, -1):
            if not squares[i]:
                continue
            if a + i <= 3:
                squares[a + i] += squares[i]
            else:
                ans += squares[i]
            squares[i] = 0

    print(ans)


if __name__ == "__main__":
    main()
