def main():
    S = [input() for _ in range(8)]
    ans = ""
    for i, s in enumerate(S):
        if "*" in s:
            for j, ss in enumerate(s):
                if ss == "*":
                    ans += chr(j + ord("a"))
                    break
            ans += str(8 - i)
            break
    print(ans)


if __name__ == "__main__":
    main()
