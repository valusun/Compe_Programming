def main():
    N = int(input())
    A = list(list(map(int, input().split())) for _ in range(N))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                x1, y1 = A[i]
                x2, y2 = A[j]
                x3, y3 = A[k]
                if abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) > 0:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
