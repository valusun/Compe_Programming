x1,y1,x2,y2 = map(int,input().split())
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

for i in range(8):
    x = x1+dx[i]
    y = y1+dy[i]
    if (x1-x)**2+(y1-y)**2 == (x2-x)**2+(y2-y)**2 == 5:
        print("Yes")
        break
else:
    print("No")