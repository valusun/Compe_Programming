def main():
    n, d = map(int, input().split())
    t = list(map(int, input().split()))
    for i in range(1, n):
        if t[i] - t[i - 1] <= d:
            print(t[i])
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()
