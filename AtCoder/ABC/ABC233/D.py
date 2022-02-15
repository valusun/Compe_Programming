N,K = map(int,input().split())
A = list(map(int,input().split()))

# 累積和
Cusum = [0]
for i in range(N):
    Cusum.append(Cusum[-1]+A[i])

Ans = 0
dic = dict()
for i in range(N):
    if Cusum[i] not in dic:
        dic[Cusum[i]] = 0
    dic[Cusum[i]]+=1
    if Cusum[i+1]-K in dic:
        Ans += dic[Cusum[i+1]-K]

print(Ans)