def main():
    _ = int(input())
    f = input()
    r_cnt = f.count("R")
    ans = 0
    for i, s in enumerate(f):
        if s == "R" and r_cnt <= i:
            ans += 1
    print(min(ans, r_cnt))


if __name__ == "__main__":
    main()
