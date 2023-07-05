from collections import defaultdict


def main():
    N = int(input())
    box = [[] for _ in range(N)]
    card_to_box_id = defaultdict(set)
    Q = int(input())
    for i in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            c, b = q[1], q[2]
            box[b - 1].append(c)
            card_to_box_id[c].add(b)
        elif q[0] == 2:
            print(*sorted(box[q[1] - 1]))
        else:
            print(*sorted(list(card_to_box_id[q[1]])))


if __name__ == "__main__":
    main()
