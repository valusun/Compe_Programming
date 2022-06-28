def main():
    def Judge(s, idx):
        for i in range(N):
            if i == idx:
                continue
            if s in names[i]:
                return False
        return True

    N = int(input())
    names = [input().split() for _ in range(N)]
    for i in range(N):
        s, t = names[i]
        if not (Judge(s, i) or Judge(t, i)):
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
