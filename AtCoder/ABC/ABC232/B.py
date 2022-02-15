S = input()
T = input()

for k in range(26):
    for i in range(len(S)):
        s = chr((ord(S[i])-97+k)%26+97)
        if s != T[i]:
            break
    else:
        print("Yes")
        exit()

print("No")