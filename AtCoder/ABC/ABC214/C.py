def main():
    N = int(input())
    A = list(map(int, input().split()))
    T = list(map(int, input().split()))

    def GetFirstJewel(fast_get_jewel):
        first_get_jewels = [fast_get_jewel]
        for i in range(1, N):
            first_get_jewels.append(min(T[i], first_get_jewels[-1] + A[i - 1]))
        return first_get_jewels

    ans = GetFirstJewel(T[0])
    if ans[-1] + A[-1] < T[0]:
        ans = GetFirstJewel(ans[-1] + A[-1])
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
