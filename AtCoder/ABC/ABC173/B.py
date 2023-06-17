from collections import Counter


def main():
    N = int(input())
    c = Counter(input() for _ in range(N))
    for k in ["AC", "WA", "TLE", "RE"]:
        print(f"{k} x {c[k]}")


if __name__ == "__main__":
    main()
