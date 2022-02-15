S,T,X = map(int,input().split())

if S<T:
    if S<=X<T:
        print("Yes")
    else:
        print("No")
else:
    if S<=X<=24 or 0<=X<T:
        print("Yes")
    else:
        print("No")