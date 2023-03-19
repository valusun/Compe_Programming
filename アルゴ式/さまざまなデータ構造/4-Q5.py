def main():
    N, Q = map(int, input().split())
    prev = [-1] * N
    nxt = [-1] * N
    for _ in range(Q):
        n, *query = map(int, input().split())
        if n == 0:
            p, q = query[0], query[1]
            nxt[p] = q
            prev[q] = p
        else:
            r = query[0]
            if nxt[r] != -1:
                prev[nxt[r]] = prev[r]
            if prev[r] != -1:
                nxt[prev[r]] = nxt[r]
            prev[r] = nxt[r] = -1
    ans, current = 0, 0
    while current != -1:
        current = prev[current]
        ans += 1
    current = 0
    while current != -1:
        current = nxt[current]
        ans += 1
    print(ans - 1)


if __name__ == "__main__":
    main()
