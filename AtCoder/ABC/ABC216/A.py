X,Y = map(int,input().split('.'))
if 0<=Y<=2:
    print(X,'-',sep="")
if 3<=Y<=6:
    print(X)
if 7<=Y<=9:
    print(X,"+",sep="")