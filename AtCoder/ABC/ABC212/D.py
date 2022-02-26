import heapq

Q = int(input())
A = []
heapq.heapify(A)

diff = 0
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        heapq.heappush(A, query[1]-diff)
    elif query[0] == 2:
        diff += query[1]
    else:
        print(heapq.heappop(A)+diff)
