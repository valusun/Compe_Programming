N = int(input())
S = dict()

for _ in range(N):
    s = input()
    if s not in S:
        S[s] = 0
    S[s]+=1

print(max(S.items(), key=lambda x:x[1])[0])