import sys
sys.setrecursionlimit(10**9)

H,W = map(int,input().split())
Field = [list(input()) for _ in range(H)]

dh = [1,0]
dw = [0,1]

Ans = 1
def dfs(h,w,d):
    global Ans
    Field[h][w] = "#"
    for i in range(2):
        next_h = h+dh[i]
        next_w = w+dw[i]
        if 0<=next_h<H and 0<=next_w<W and Field[next_h][next_w] == ".":
            d+=1
            Ans = max(Ans, d)
            dfs(next_h, next_w, d)
            d-=1

dfs(0,0,1)
print(Ans)