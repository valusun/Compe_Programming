def gcd(x, y):
    if x%y==0: return y
    else: return gcd(y, x%y)

N = int(input())
x,y = [],[]
for i in range(N):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

Ans = set()
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        X,Y = x[j]-x[i], y[j]-y[i]
        if X == 0:
            Ans.add((0, Y//abs(Y)))
        elif Y == 0:
            Ans.add((X//abs(X), 0))
        else:
            Z = abs(gcd(X,Y))
            Ans.add((X//Z, Y//Z))

print(len(Ans))
        