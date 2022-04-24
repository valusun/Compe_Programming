def rotate(S):
    return list(zip(*S[::-1]))


def FindLeftTop(N, X):
    for i in range(N):
        for j in range(N):
            if X[i][j] == "#":
                return i, j


def IsSame(N, S, T):
    si, sj = FindLeftTop(N, S)
    ti, tj = FindLeftTop(N, T)
    offset_i = ti - si
    offset_j = tj - sj
    for i in range(N):
        for j in range(N):
            t_i = i + offset_i
            t_j = j + offset_j
            if 0 <= t_i < N and 0 <= t_j < N:
                if S[i][j] != T[t_i][t_j]:
                    return False
            else:
                if S[i][j] == "#":
                    return False
    return True


def main():
    N = int(input())
    S = list(list(input()) for _ in range(N))
    T = list(list(input()) for _ in range(N))
    if sum(s.count("#") for s in S) != sum(t.count("#") for t in T):
        print("No")
        exit()
    for _ in range(4):
        if IsSame(N, S, T):
            print("Yes")
            break
        S = rotate(S)
    else:
        print("No")


if __name__ == "__main__":
    main()
