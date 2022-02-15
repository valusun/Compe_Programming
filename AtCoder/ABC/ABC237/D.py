N = int(input())
S = input()

L,R = [],[]
for i in range(N):
    if S[i] == 'L':
        R.append(i)
    else:
        L.append(i)

print(*L,N,*R[::-1])