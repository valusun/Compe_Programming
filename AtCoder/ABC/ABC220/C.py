N = int(input())
A = list(map(int,input().split()))
X = int(input())

B = sum(A)
Now = X//B*B
Ans = X//B*N

i = 0
while Now <= X:
    Now+=A[i]
    Ans+=1
    i+=1

print(Ans)