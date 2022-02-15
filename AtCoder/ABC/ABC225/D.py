N,Q = map(int,input().split())

# 双方向連結リスト(train[i][0]..i番目の先頭に繋がっている車両 / [1]は後ろに繋がっている車両)
train = [[-1,-1] for _ in range(N)]

for i in range(Q):
    # tの後は可変 /*aにすることで、リスト型で受け取れるので便利
    t,*a = map(int,input().split())
    if t == 1:
        x,y = a[0]-1,a[1]-1
        train[x][1] = y
        train[y][0] = x
    elif t == 2:
        x,y = a[0]-1, a[1]-1
        train[x][1] = -1
        train[y][0] = -1
    else:
        x = a[0]-1
        while train[x][0] != -1:
            x = train[x][0]
        Ans = []
        while train[x][1] != -1:
            Ans.append(x+1)
            x = train[x][1]
        Ans.append(x+1)
        print(len(Ans),*Ans)