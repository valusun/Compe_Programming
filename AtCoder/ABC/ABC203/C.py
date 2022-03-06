N,K = map(int,input().split())
town = sorted(list(map(int,input().split())) for _ in range(N))
town.append([10**30, 0])

ans = 0
now = 0
for i in range(N):
    if K < (town[i][0]-now):
        break
    K = K-(town[i][0]-now)+town[i][1]
    now = town[i][0]
    i+=1
print(now+K)