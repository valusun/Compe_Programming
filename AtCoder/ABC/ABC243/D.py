N,X = map(int,input().split())
S = input()

stack = []
for i in range(N):
    if len(stack):
        if stack[-1] == 'U':
            stack.append(S[i])
        else:
            if S[i] == 'U':
                stack.pop()
            else:
                stack.append(S[i])
    else:
        stack.append(S[i])

for s in stack:
    if s=='U':
        X//=2
    elif s=='L':
        X*=2
    else:
        X = X*2+1
print(X)