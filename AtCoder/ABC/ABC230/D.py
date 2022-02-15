N,D = map(int,input().split())
Wall = [list(map(int,input().split())) for _ in range(N)]
Wall = sorted(Wall, key = lambda x:x[1])

Now = Wall[0][1]
Ans = 1
for i in range(1, N):
    if Wall[i][0] > Now+D-1:
        Ans+=1
        Now = Wall[i][1]

print(Ans)