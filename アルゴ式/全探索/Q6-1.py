def main():
    _, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i, a1 in enumerate(A):
        for a2 in A[i + 1 :]:
            if a1 + a2 <= K:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
