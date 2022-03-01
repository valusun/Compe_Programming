N,K = map(int,input().split())
C = list(map(int,input().split()))

cnt = 0
dic = dict()
for i in range(K):
    if C[i] not in dic:
        dic[C[i]] = 0
        cnt+=1
    dic[C[i]]+=1

Ans = cnt
l = 0
for i in range(K,N):
    if C[i] not in dic:
        dic[C[i]] = 0
        cnt+=1
    dic[C[i]]+=1

    dic[C[l]]-=1
    if dic[C[l]]==0:
        dic.pop(C[l])
        cnt-=1
    
    Ans = max(Ans, cnt)
    l+=1

print(Ans)
