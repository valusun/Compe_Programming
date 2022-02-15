N,X = map(int,input().split())
A = list(map(int,input().split()))

Check = [0]*N
Ans = 0
while True:
    if Check[X-1]:
        print(Ans)
        break
    Check[X-1]=1
    Ans+=1
    X = A[X-1]