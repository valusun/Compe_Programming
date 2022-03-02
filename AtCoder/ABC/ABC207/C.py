N = int(input())
AB = []
for i in range(N):
    t,x,y = map(int,input().split())
    if t==2: y-=0.1
    if t==3: x+=0.1
    if t==4: x,y = x+0.1,y-0.1
    AB.append([x,y])

Ans = 0
for i in range(N):
    for j in range(i+1,N):
        if max(AB[i][0], AB[j][0]) <= min(AB[i][1], AB[j][1]):
            Ans+=1

print(Ans)