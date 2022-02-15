N,K,A = map(int,input().split())

Ans = (A+K-1)%N
if Ans==0: Ans=N
print(Ans)