import heapq

N,K = map(int,input().split())
P = list(map(int,input().split()))

# 優先度付きキューの作成
A = []
heapq.heapify(A)

# K個目まで値を入れる
for i in range(K):
    heapq.heappush(A, P[i])

for i in range(K, N):
    Ans = heapq.heappop(A)
    print(Ans)

    # 追加する値(P[i])と比較し、大きい方をAに入れる
    heapq.heappush(A, max(Ans, P[i]))

# 最後の出力だけ行っていないのでここで行っておく
print(heapq.heappop(A))