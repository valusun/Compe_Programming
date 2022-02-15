N = int(input())
A,B = [],[]
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

Time = 0
for i in range(N):
    Time += A[i]/B[i]/2

Ans = 0
time = 0
for i in range(N):
    t = A[i]/B[i]
    if time+t <= Time:
        time += t
        Ans += A[i]
    else:
        Ans += (Time-time)*B[i]
        break
print(Ans)