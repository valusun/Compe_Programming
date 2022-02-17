A,B,C = map(int,input().split())
D = B//C*C
if A<=D<=B:
    print(D)
else:
    print(-1)
