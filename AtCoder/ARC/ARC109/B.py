def main():
    n = int(input())
    tree_cutting_number = 0
    tree_length = n + 1

    low = 0
    high = tree_length
    while abs(high - low) > 1:
        mid = (low + high) // 2
        if mid * (mid + 1) // 2 <= tree_length:
            tree_cutting_number = max(tree_cutting_number, mid)
            low = mid
        else:
            high = mid
    print(n - tree_cutting_number + 1)


if __name__ == "__main__":
    main()
