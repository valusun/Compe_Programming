N = int(input())
A = list(map(int,input().split()))

A200 = [0]*200
for i in range(N):
    A200[A[i]%200]+=1

Ans = 0
for i in range(200):
    Ans += (A200[i]*(A200[i]-1)//2)
print(Ans)