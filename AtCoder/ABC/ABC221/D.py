N = int(input())
AB = []
for i in range(N):
    a,b = map(int,input().split())
    AB.append([a, 1])
    AB.append([a+b, -1])
AB.sort()

Ans = [0]*(N+1)
now = 0
for i in range(N*2-1):
    now += AB[i][1]
    Ans[now] += (AB[i+1][0] - AB[i][0])
print(*Ans[1:])