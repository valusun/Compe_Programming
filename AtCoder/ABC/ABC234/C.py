def exchange(x):
    ret = ""
    while x:
        tmp = x%2
        if tmp == 1:
            ret += "2"
        else:
            ret += "0"
        x//=2
    return ret[::-1]

K = int(input())
print(exchange(K))