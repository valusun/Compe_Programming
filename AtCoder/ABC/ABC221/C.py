N = list(input())

Ans = 0
for i in range(2**len(N)):
    t1,t2 =  [],[]
    for j in range(len(N)):
        if i&(1<<j):
            t1.append(N[j])
        else:
            t2.append(N[j])
    if len(t1)==0 or len(t2)==0:
        continue
    t1.sort(reverse=True)
    t2.sort(reverse=True)
    t1 = "".join(t1)
    t2 = "".join(t2)
    Ans = max(Ans, int(t1)*int(t2))

print(Ans)