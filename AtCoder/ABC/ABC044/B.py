from collections import Counter


def main():
    W = input()
    c = Counter()
    for w in W:
        c[w] += 1
    for val in c.values():
        if val % 2:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
