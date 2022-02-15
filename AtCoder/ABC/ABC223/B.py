S = input()

C = []
for i in range(len(S)):
    tmp = S[i:]+S[0:i]
    C.append(tmp)

C.sort()
print(C[0], C[-1], sep="\n")