a,b,c = map(int,input().split())

if a!=b and a!=c and b!=c:
    print(0)
elif b==c:
    print(a)
elif a==c:
    print(b)
else:
    print(c)