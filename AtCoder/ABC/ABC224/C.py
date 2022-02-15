N = int(input())
Xy = [list(map(int,input().split())) for _ in range(N)]

Ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            x1,y1 = Xy[i]
            x2,y2 = Xy[j]
            x3,y3 = Xy[k]
            if abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3)) > 0:
                Ans+=1

print(Ans)