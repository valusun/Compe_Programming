def IsCheck(a, x):
    x = sum(a) - x
    if x < 0:
        return False
    n = len(a)
    dp = [False] * (x + 1)
    dp[0] = True
    for i in range(1, n):
        for j in range(x, -1, -1):
            if j - (a[i] * 2) >= 0:
                dp[j] |= dp[j - (a[i] * 2)]
    return dp[x]


def main():
    S = input()
    end_x, end_y = map(int, input().split())
    x, y = [], [0]
    t_cnt, f_cnt = 0, 0
    for s in S:
        if s == "F":
            f_cnt += 1
        else:
            if t_cnt % 2 == 0:
                x.append(f_cnt)
            else:
                y.append(f_cnt)
            f_cnt = 0
            t_cnt += 1
    if t_cnt % 2 == 0:
        x.append(f_cnt)
    else:
        y.append(f_cnt)
    print(x)
    if IsCheck(x, end_x) and IsCheck(y, end_y):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
