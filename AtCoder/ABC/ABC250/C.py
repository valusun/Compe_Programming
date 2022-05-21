def main():
    N, Q = map(int, input().split())
    val = list(range(1, N + 1))
    val_idx = list(range(N))
    for _ in range(Q):
        idx = val_idx[int(input()) - 1]
        if idx == N - 1:
            x, y = idx - 1, idx
        else:
            x, y = idx, idx + 1
        val_x, val_y = val[x] - 1, val[y] - 1
        val[x], val[y] = val[y], val[x]
        val_idx[val_x], val_idx[val_y] = val_idx[val_y], val_idx[val_x]

    print(*val)


if __name__ == "__main__":
    main()
