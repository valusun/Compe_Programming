S = input()

ans = ""
for i in S:
    if i=='6':
        ans+='9'
    elif i=='9':
        ans+='6'
    else:
        ans+=i
print(ans[::-1])