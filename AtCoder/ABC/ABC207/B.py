A,B,C,D = map(int,input().split())
if B>=C*D:
    print(-1)
else:
    Blue = A
    Red = 0
    cnt = 0
    while A>Red*D:
        A+=B
        Red+=C
        cnt+=1
    print(cnt)