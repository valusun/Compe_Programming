def main():
    _ = int(input())
    W = list(input().split())
    tgts = ("and", "not", "that", "the", "you")
    for w in W:
        if w in tgts:
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()
