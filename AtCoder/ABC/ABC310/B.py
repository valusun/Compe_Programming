def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            pi, pj = A[i][0], A[j][0]
            fi, fj = set(A[i][2:]), set(A[j][2:])
            has = all([_fi in fj for _fi in list(fi)])
            if pi >= pj and has and (pi > pj or len(fj) > len(fi)):
                print("Yes")
                exit()
    print("No")


if __name__ == "__main__":
    main()
