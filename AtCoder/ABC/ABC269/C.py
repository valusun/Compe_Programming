def main():
    N = int(input())
    one = []
    for i in range(60):
        if N & (1 << i):
            one.append(i)
    n = len(one)
    # 配列の中身をbit全探索(O(2^15))
    for i in range(1 << n):
        ans = 0
        for j in range(n):
            if i & (1 << j):
                ans |= 1 << one[j]
        print(ans)


if __name__ == "__main__":
    main()
