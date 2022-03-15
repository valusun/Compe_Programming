N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

x,y = 0,0
for i in range(N):
    if A[i] in set(B):
        if A[i] == B[i]:
            x+=1
        else:
            y+=1

print(x,y)