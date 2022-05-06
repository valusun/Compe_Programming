def Offset(t, x, y):
    if t == 1:
        return x, y
    if t == 2:
        return x, y - 0.1
    if t == 3:
        return x + 0.1, y
    if t == 4:
        return x + 0.1, y - 0.1


def main():
    N = int(input())
    A = [Offset(*map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if max(A[i][0], A[j][0]) <= min(A[i][1], A[j][1]):
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
