def main():
    sections = [0] * 102
    a, b, c, d = map(int, input().split())
    sections[a] += 1
    sections[b] -= 1
    sections[c] += 1
    sections[d] -= 1
    for i in range(101):
        sections[i + 1] += sections[i]
    print(sections.count(2))


if __name__ == "__main__":
    main()
