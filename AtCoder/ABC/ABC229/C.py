N,W = map(int,input().split())
Cheese = [list(map(int,input().split())) for _ in range(N)]

Cheese.sort(reverse=True)
Ans = 0

i = 0
while N>i:
    if W >= Cheese[i][1]:
        Ans += Cheese[i][0]*Cheese[i][1]
        W -= Cheese[i][1]
    else:
        Ans += Cheese[i][0]*W
        break
    i+=1

print(Ans)