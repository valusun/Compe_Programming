def main():
    N = int(input())
    prev = [-1] * N
    nxt = [-1] * N
    for i in range(N):
        nxt[i] = i + 1
        if i + 1 == N:
            nxt[i] = 0
        prev[i] = i - 1
        if prev[i] == -1:
            prev[i] = N - 1
    excluded_num = 0
    for i in range(N - 1):
        prev[nxt[excluded_num]] = prev[excluded_num]
        nxt[prev[excluded_num]] = nxt[excluded_num]
        excluded_num = nxt[nxt[excluded_num]]
    print(excluded_num + 1)  # 0-indexのため


if __name__ == "__main__":
    main()
