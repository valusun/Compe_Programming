import heapq
from collections import deque

Query = int(input())
Queue = deque()
sort_end = []

for i in range(Query):
    t,*x = map(int,input().split())
    if t==1:
        Queue.append(x[0])
    elif t==2:
        if len(sort_end):
            print(heapq.heappop(sort_end))
        else:
            print(Queue.popleft())
    else:
        while len(Queue):
            heapq.heappush(sort_end, Queue.popleft())