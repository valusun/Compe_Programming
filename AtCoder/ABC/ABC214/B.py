S,T = map(int,input().split())

Ans = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i+j+k<=S and i*j*k<=T:
                Ans+=1
print(Ans)