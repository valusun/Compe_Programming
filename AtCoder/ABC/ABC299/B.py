from collections import defaultdict


def main():
    N, T = map(int, input().split())
    C = list(map(int, input().split()))
    R = list(map(int, input().split()))
    dic = defaultdict(list)
    for i in range(N):
        dic[C[i]].append((R[i], i + 1))
    if T not in dic:
        T = C[0]
    print(sorted(dic[T], reverse=True)[0][1])


if __name__ == "__main__":
    main()
