def main():
    N = int(input())
    logins_logs = []
    for _ in range(N):
        a, b = map(int, input().split())
        logins_logs.append([a, 1])
        logins_logs.append([a + b, -1])
    logins_logs.sort()
    login_cnts = [0] * (N + 1)
    now_login = 0
    for i in range(N * 2 - 1):
        now_login += logins_logs[i][1]
        login_cnts[now_login] += logins_logs[i + 1][0] - logins_logs[i][0]
    print(*login_cnts[1:])


if __name__ == "__main__":
    main()
