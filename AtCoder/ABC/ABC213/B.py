N = int(input())
A = list(map(int,input().split()))
X = [[A[i],i+1] for i in range(N)]
X.sort()
print(X[-2][1])
