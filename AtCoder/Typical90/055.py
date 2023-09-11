def main():
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for a1 in range(N):
        for a2 in range(a1 + 1, N):
            for a3 in range(a2 + 1, N):
                for a4 in range(a3 + 1, N):
                    for a5 in range(a4 + 1, N):
                        res = A[a1] % P * A[a2] % P * A[a3] % P * A[a4] % P * A[a5] % P
                        if res == Q:
                            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
