def main():
    N, _ = map(int, input().split())
    A = list(map(int, input().split()))
    seq = list(range(1, N + 1))
    f = [0] * N
    for a in A:
        f[a - 1] += 1
    ans = []
    s = 0
    for i in range(N):
        if f[i] == 0:
            ans += seq[s : i + 1][::-1]
            s = i + 1
    if f[-1] == 1:
        ans += seq[s : i + 1][::-1]
    print(*ans)


if __name__ == "__main__":
    main()
