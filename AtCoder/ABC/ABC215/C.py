from itertools import permutations

S,K = input().split()
S = list(S)
K = int(K)
S_per = set("".join(i) for i in permutations(S))
S_per = list(sorted(S_per))
print(S_per[K-1])