N = int(input())

Ans = ""
while N:
    if N%2==0:
        N//=2
        Ans+="B"
    else:
        N-=1
        Ans+="A"

print(Ans[::-1])