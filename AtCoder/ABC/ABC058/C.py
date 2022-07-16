import string


def main():
    N = int(input())
    words = [input() for _ in range(N)]
    MAX_LENGTH = 51
    alphabet_counts = dict.fromkeys(string.ascii_lowercase, MAX_LENGTH)
    for word in words:
        for s in alphabet_counts.keys():
            alphabet_counts[s] = min(alphabet_counts[s], word.count(s))
    ans = ""
    for s, v in alphabet_counts.items():
        ans += s * v
    print(ans)


if __name__ == "__main__":
    main()
