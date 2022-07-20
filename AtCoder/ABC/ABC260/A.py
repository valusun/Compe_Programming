from typing import Counter


def main():
    S = input()
    c = Counter()
    for s in S:
        c[s] += 1
    for s in S:
        if c[s] == 1:
            print(s)
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()
