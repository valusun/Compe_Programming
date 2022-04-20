def calc(b):
    return a**3 + a**2 * b + a * b**2 + b**3


N = int(input())
ok = 10**6 + 1
ng = 0
ans = 10**6 + 1
for a in range(10**6 + 1):
    ok = 10**6 + 1
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if calc(mid) >= N:
            ok = mid
        else:
            ng = mid
    ans = min(ans, calc(ok))
print(ans)
