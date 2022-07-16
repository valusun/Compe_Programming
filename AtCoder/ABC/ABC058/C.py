from collections import defaultdict


def GenerateStandardDict(word: str):
    """アルファベットと出現回数を記録した辞書を作る"""

    alphabet_counts = defaultdict(int)
    for s in sorted(word):
        alphabet_counts[s] += 1
    return alphabet_counts


def main():
    N = int(input())
    words = [input() for _ in range(N)]
    alphabet_counts = GenerateStandardDict(words[0])
    for word in words[1:]:
        for s in alphabet_counts.keys():
            alphabet_counts[s] = min(alphabet_counts[s], word.count(s))
    ans = ""
    for s, v in alphabet_counts.items():
        ans += s * v
    print(ans)


if __name__ == "__main__":
    main()
