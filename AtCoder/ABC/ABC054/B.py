def main():
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(N)]
    B = [list(input()) for _ in range(M)]
    for ai in range(N - M + 1):
        for aj in range(N - M + 1):
            ok_flag = True
            for bi in range(M):
                for bj in range(M):
                    if A[ai + bi][aj + bj] != B[bi][bj]:
                        ok_flag = False
                        break
            if ok_flag:
                print("Yes")
                exit()
    print("No")


if __name__ == "__main__":
    main()
