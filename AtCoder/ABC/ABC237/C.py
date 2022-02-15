S = input()
N = len(S)

# 先頭のaの数
i = 0
while i<N and S[i]=='a':
    i+=1
First = i

# 末尾のaの数
i = 0
while i<N and S[-i-1]=='a':
    i+=1
End = i

S = 'a'*(max(0, End-First)) + S
N = len(S)

for i in range(N//2):
    if S[i] != S[-i-1]:
        print("No")
        break
else:
    print("Yes")