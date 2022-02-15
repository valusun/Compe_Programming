from math import sqrt

N = int(input())
sq = int(sqrt(N))+1

Ans = 0
for i in range(1, sq):
    Ans += (N//i-i)*2
    Ans+=1

print(Ans)