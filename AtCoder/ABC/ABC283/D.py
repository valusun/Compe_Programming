def main():
    S = input()
    boxes = [[] for _ in range(len(S))]
    used = [False] * 26
    left = 0
    for s in S:
        if s == "(":
            left += 1
        elif s == ")":
            for u in boxes[left]:
                used[ord(u) - 97] = False
            boxes[left] = []
            left -= 1
        else:
            if used[ord(s) - 97]:
                print("No")
                break
            boxes[left].append(s)
            used[ord(s) - 97] = True
    else:
        print("Yes")


if __name__ == "__main__":
    main()
