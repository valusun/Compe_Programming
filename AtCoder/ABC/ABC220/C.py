def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    total_A = sum(A)
    addable_A_cnt = X // total_A
    total_A *= addable_A_cnt
    ans = addable_A_cnt * N
    for a in A:
        if total_A > X:
            break
        total_A += a
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
