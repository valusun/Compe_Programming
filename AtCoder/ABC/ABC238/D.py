def CHECK(a,s):
    # [x + y = s]部
    if 2*a > s:
        return "No"
    
    # Lを求め、2進数とその長さを求めておく
    L = s-2*a
    L_bin = bin(L)[2:]
    L_len = len(L_bin)

    # aの2進数を求めておく
    a_bin = bin(a)[2:]

    # Lを基準に見るので、Lの長さに合わせて0埋めを行う
    a_bin = a_bin.zfill(L_len)

    # 2**kとした方が分かりやすいので、どちらの2進数も逆順にしておく
    L_bin = L_bin[::-1]
    a_bin = a_bin[::-1]

    # 2進数をチェックしていく
    for k in range(L_len):
        # 0は変化させなくてよい
        if L_bin[k] == '0':
            continue
        # a[k]=1ならば、変化させてはいけないので、L=0が達成出来ないのでNo
        if a_bin[k] == '1':
            return "No"
    return "Yes"

T = int(input())
for i in range(T):
    a,s = map(int,input().split())
    print(CHECK(a,s))