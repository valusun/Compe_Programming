def main():
    S = input()
    ans = []
    for s in S:
        if s != "B":
            ans.append(s)
        elif ans:
            ans.pop()
    print("".join(ans))


if __name__ == "__main__":
    main()
