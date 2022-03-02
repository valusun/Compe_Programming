from bisect import bisect_right

P = int(input())

Num = [1]
for i in range(2, 11):
    Num.append(Num[-1]*i)

Ans = 0
while P:
    x = bisect_right(Num, P)-1
    Ans += P//Num[x]
    P -= Num[x]*(P//Num[x])
print(Ans)