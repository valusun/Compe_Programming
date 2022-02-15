from collections import deque

# ----- 入力 ----- #
M = int(input())
Graph = [[] for _ in range(9)]
for i in range(M):
    v,u = map(int,input().split())
    Graph[v-1].append(u-1)
    Graph[u-1].append(v-1)
p = list(map(int,input().split()))


# ----- コマ[i]がどこに置かれているかの情報に書き換える(0-index) ----- #
koma_on_Graph = ["8"]*9
for i in range(8):
    koma_on_Graph[p[i]-1] = str(i)
print(koma_on_Graph)


# ----- コマを動かした盤面を記録 ----- #
Seen = set()
koma_on_Graph_str = "".join(koma_on_Graph)
Seen.add(koma_on_Graph_str)


# ----- 終了状態 ----- #
Goal = [str(i) for i in range(9)]


# ----- bfsで動かしていく ----- #
Q = deque()
Q.append((koma_on_Graph, 0))
while Q:
    status, d = Q.popleft()
    if status == Goal:
        print(d)
        break
    # コマが乗っていないGraphの場所を見つける
    space = status.index('8')
    for i in Graph[space]:
        # 入れ替えるためにコピーする
        status_copy = status[:]
        status_copy[space], status_copy[i] = status_copy[i], status_copy[space]
        # 入れ替えた後の盤面が以前出ていたら記録しない
        status_copy_str = "".join(status_copy)
        if status_copy_str not in Seen:
            Seen.add(status_copy_str)
            Q.append((status_copy, d+1))
else:
    print(-1)