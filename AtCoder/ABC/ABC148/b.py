def main():
    N = int(input())
    S, T = input().split()
    ans = "".join(f"{S[i]}{T[i]}" for i in range(N))
    print(ans)


if __name__ == "__main__":
    main()
