N = int(input())
S = list(map(int,input().split()))

Ans = set()
for a in range(1, 200):
    for b in range(1, 200):
        Ans.add(4*a*b+3*a+3*b)

res = 0
for i in range(N):
    if S[i] not in Ans:
        res+=1

print(res)