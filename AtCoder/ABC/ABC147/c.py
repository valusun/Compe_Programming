def main():
    N = int(input())
    A = []
    for _ in range(N):
        k = int(input())
        A.append([list(map(int, input().split())) for _ in range(k)])
    ans = 0
    for bit in range(2**N):
        cnt = 0
        for i in range(N):
            if not (bit & (1 << i)):
                continue
            cnt += 1
            is_ok = True
            for x, y in A[i]:
                x = x - 1
                is_honest = bit & (1 << x)
                # xが「正直者」なのに、「不親切な人」の場合
                if y and not is_honest:
                    is_ok = False
                # xが「不親切の人」なのに、「正直者」の場合
                if not y and is_honest:
                    is_ok = False
            if not is_ok:
                break
        else:
            ans = max(ans, cnt)
    print(ans)


if __name__ == "__main__":
    main()
