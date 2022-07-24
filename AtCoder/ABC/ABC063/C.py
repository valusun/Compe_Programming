def main():
    N = int(input())
    S = [int(input()) for _ in range(N)]

    ans = sum(S)
    if ans % 10:
        print(ans)
    else:
        S.sort()
        for s in S:
            if s % 10 == 0:
                continue
            ans -= s
            if ans % 10:
                print(ans)
                break
        else:
            print(0)


if __name__ == "__main__":
    main()
