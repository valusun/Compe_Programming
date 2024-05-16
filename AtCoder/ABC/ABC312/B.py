def main():

    def judge(si, sj):
        # 左上
        for i in range(4):
            for j in range(4):
                target = "." if i == 3 or j == 3 else "#"
                if S[si + i][sj + j] != target:
                    return False
        # 右下
        for i in range(4):
            for j in range(4):
                target = "." if i == 0 or j == 0 else "#"
                if S[si + i + 5][sj + j + 5] != target:
                    return False
        return True

    N, M = map(int, input().split())
    S = [list(input()) for _ in range(N)]
    for i in range(N - 8):
        for j in range(M - 8):
            if judge(i, j):
                print(f"{i+1} {j+1}")


if __name__ == "__main__":
    main()
