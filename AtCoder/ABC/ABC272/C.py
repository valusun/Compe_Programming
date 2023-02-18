def main():
    _ = int(input())
    A = list(map(int, input().split()))
    even, odd = [], []
    for a in A:
        if a % 2:
            odd.append(a)
        else:
            even.append(a)
    odd.sort(reverse=True)
    even.sort(reverse=True)
    odd_sum, even_sum = 0, 0
    if len(odd) >= 2:
        odd_sum = sum(odd[:2])
    if len(even) >= 2:
        even_sum = sum(even[:2])
    if len(odd) < 2 and len(even) < 2:
        print(-1)
    else:
        print(max(odd_sum, even_sum))


if __name__ == "__main__":
    main()
