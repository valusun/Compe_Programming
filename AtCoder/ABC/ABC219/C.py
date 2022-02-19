X = list(input())
A = "abcdefghijklmnopqrstuvwxyz"

S = int(input())

Ans = []
for i in range(S):
    tmp = ""
    s = input()
    for j in s:
        for k in range(26):
            if j == X[k]:
                tmp += chr(k+97)
    Ans.append([tmp,s])

Ans.sort()
for i in range(S):
    print(Ans[i][1])