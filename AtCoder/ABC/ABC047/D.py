from collections import defaultdict


def main():
    _ = map(int, input().split())
    A = list(map(int, input().split()))
    prof_cnts = defaultdict(int)
    buying_value, selling_value = A[0], A[0]
    for a in A[1:]:
        if a < buying_value:
            prof = selling_value - buying_value
            prof_cnts[prof] += 1
            buying_value = a
            selling_value = a
        else:
            selling_value = max(selling_value, a)
    prof = selling_value - buying_value
    prof_cnts[prof] += 1
    print(prof_cnts)
    print(sorted(prof_cnts.items())[-1][1])


if __name__ == "__main__":
    main()
