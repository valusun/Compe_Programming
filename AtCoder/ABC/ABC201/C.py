S = input()

Ans = 0
for i in range(10000):
    Flag = [0]*10
    number = i
    for j in range(4):
        Flag[number%10] = 1
        number//=10
    for j in range(10):
        if Flag[j]==1 and S[j]=='x':
            break
        if Flag[j]==0 and S[j]=='o':
            break
    else:
        Ans+=1

print(Ans)