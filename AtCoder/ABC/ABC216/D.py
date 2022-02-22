from collections import deque

N,M = map(int,input().split())
A = []
Top_Balls = [[] for _ in range(N+1)]
Q = deque()
for i in range(M):
    x = int(input())
    A.append(deque(map(int,input().split())))
    Top_Balls[A[i][0]].append(i)
    if len(Top_Balls[A[i][0]]) == 2:
        Q.append(A[i][0])

cnt = 0
while Q:
    i = Q.popleft()
    x,y = Top_Balls[i][0], Top_Balls[i][1]

    A[x].popleft()
    if len(A[x]):
        Top_Balls[A[x][0]].append(x)
        if len(Top_Balls[A[x][0]])==2:
            Q.append(A[x][0])
    
    A[y].popleft()
    if len(A[y]):
        Top_Balls[A[y][0]].append(y)
        if len(Top_Balls[A[y][0]])==2:
            Q.append(A[y][0])
    cnt+=1

if cnt == N:
    print("Yes")
else:
    print("No")