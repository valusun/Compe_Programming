def main():
    _, X = map(int, input().split())
    S = input()
    stack = []
    for s in S:
        if stack and s == "U" and stack[-1] != "U":
            stack.pop()
        else:
            stack.append(s)

    for s in stack:
        if s == "U":
            X //= 2
        elif s == "L":
            X *= 2
        else:
            X = (X * 2) + 1
    print(X)


if __name__ == "__main__":
    main()
