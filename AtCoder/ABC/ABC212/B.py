X = list(input())
S_set = set(X)

if len(S_set) == 1:
    print("Weak")
    exit()

for i in range(3):
    if not ((int(X[i])+1 == int(X[i+1])) or (X[i]=='9' and X[i+1]=='0')):
        print("Strong")
        break
else:
    print("Weak")