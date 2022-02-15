N = int(input())
B = list(map(int,input().split()))

cut = [0]
for i in range(N):
    if cut[-1]+B[i] < 360:
        cut.append(cut[-1]+B[i])
    else:
        cut.append((cut[-1]+B[i])%360)

cut.sort()
cut.append(360)
Ans = 0
for i in range(N+1):
    Ans = max(Ans, cut[i+1]-cut[i])

print(Ans)