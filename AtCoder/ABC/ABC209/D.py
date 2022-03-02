from collections import deque

N,Q = map(int,input().split())
Graph = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    Graph[a-1].append(b-1)
    Graph[b-1].append(a-1)

Queue = deque()
Queue.append((0,1))
Color = [-1]*N
Color[0] = 0
while Queue:
    v,col = Queue.popleft()
    for i in Graph[v]:
        if Color[i]==-1:
            Color[i]=col
            Queue.append((i,(col+1)%2))

for i in range(Q):
    x,y = map(int,input().split())
    if Color[x-1] == Color[y-1]:
        print("Town")
    else:
        print("Road")