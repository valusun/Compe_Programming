from collections import Counter


def main():
    N = int(input())
    c = Counter()
    for _ in range(N):
        s = input()
        if s not in c:
            print(s)
        else:
            print(f"{s}({c[s]})")
        c[s] += 1


if __name__ == "__main__":
    main()
