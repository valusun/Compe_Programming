S = input()
K = int(input())
len_S = len(S)

Cusum = [0]
for i in range(len_S):
    if S[i]=='.':
        Cusum.append(Cusum[-1]+1)
    else:
        Cusum.append(Cusum[-1])

Ans = 0
r = 0
for l in range(len_S):
    while r<len_S and Cusum[r+1]-Cusum[l]<=K:
        r+=1
    Ans = max(Ans, r-l)

print(Ans)