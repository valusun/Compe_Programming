def main():
    _ = int(input())
    s = input()
    ans = ""
    for i in s:
        ans += i
        if len(ans) > 2 and ans[-3:] == "fox":
            ans = ans[:-3]
    print(len(ans))


if __name__ == "__main__":
    main()
