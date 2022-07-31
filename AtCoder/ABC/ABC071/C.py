from collections import Counter


def GetRectangleArea(n):
    return n[0] * n[1] if len(n) >= 2 else 0


def GetSquareArea(n):
    return n[0] ** 2 if len(n) >= 1 else 0


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    c = Counter()
    for a in A:
        c[a] += 1
    used_candidate_rectangle, used_candidate_square = [], []
    for k, v in c.items():
        if v >= 2:
            used_candidate_rectangle.append(k)
            if v >= 4:
                used_candidate_square.append(k)
    used_candidate_rectangle.sort(reverse=True)
    used_candidate_square.sort(reverse=True)

    max_rectangle = GetRectangleArea(used_candidate_rectangle)
    max_square = GetSquareArea(used_candidate_square)
    print(max(max_rectangle, max_square))


if __name__ == "__main__":
    main()
