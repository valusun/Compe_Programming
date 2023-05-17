def main():
    N, M = map(int, input().split())
    a = [0] * N
    v = [False] * N
    for i in range(M):
        s, c = map(int, input().split())
        if v[s - 1] and a[s - 1] != c:
            print("-1")
            exit()
        a[s - 1] = c
        v[s - 1] = True
    if N != 1:
        if a[0] == 0 and v[0]:
            print(-1)
            exit()
        else:
            if a[0] == 0:
                a[0] = 1
    print("".join(str(n) for n in a))


if __name__ == "__main__":
    main()
