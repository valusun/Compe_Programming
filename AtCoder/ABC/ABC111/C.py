from collections import Counter


def main():
    N = int(input())
    sequence = list(map(int, input().split()))

    if len(set(sequence)) == 1:
        print(N // 2)
        exit()

    even_elm, odd_elm = Counter(), Counter()
    for i, n in enumerate(sequence):
        if i % 2 == 0:
            even_elm[n] += 1
        else:
            odd_elm[n] += 1

    even_used_num, even_used_cnt = even_elm.most_common()[0]
    odd_used_num, odd_used_cnt = odd_elm.most_common()[0]

    if even_used_num == odd_used_num:
        if len(odd_elm) == 1:
            even_used_cnt = even_elm.most_common()[1][1]
        elif len(even_elm) == 1:
            odd_used_cnt = odd_elm.most_common()[1][1]
        else:
            if even_elm.most_common()[1][1] < odd_elm.most_common()[1][1]:
                odd_used_cnt = odd_elm.most_common()[1][1]
            else:
                even_used_cnt = even_elm.most_common()[1][1]
    even_change_cnt = N // 2 - even_used_cnt
    odd_change_cnt = N // 2 - odd_used_cnt
    print(even_change_cnt + odd_change_cnt)


if __name__ == "__main__":
    main()
