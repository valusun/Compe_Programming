def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    # _{100}C_{5} < 10^9
    for a in range(N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                for d in range(c + 1, N):
                    for e in range(d + 1, N):
                        if A[a] + A[b] + A[c] + A[d] + A[e] == 1000:
                            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
