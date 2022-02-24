N = int(input())
A = list(map(int,input().split()))
T = list(map(int,input().split()))

Ans_tmp = [T[0]]
for i in range(1, N):
    Ans_tmp.append(min(Ans_tmp[-1]+A[i-1], T[i]))

Ans = [min(Ans_tmp[-1]+A[-1], T[0])]
for i in range(1,N):
    Ans.append(min(Ans[-1]+A[i-1], T[i]))

print(*Ans, sep="\n")