def main():
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(N - 2):
        if p[i] < p[i + 1] < p[i + 2] or p[i] > p[i + 1] > p[i + 2]:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
