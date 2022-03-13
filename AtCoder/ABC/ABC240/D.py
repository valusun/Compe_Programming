N = int(input())
A = list(map(int,input().split()))

stack = [[-1, -1]]
ball = 0
for i in range(N):
    if stack[-1][0]!=A[i]:
        stack.append([A[i], 1])
        ball+=1
    else:
        if stack[-1][1]+1 == A[i]:
            ball-=(A[i]-1)
            stack.pop()
        else:
            stack[-1][1]+=1
            ball+=1
    print(ball)
    