def main():
    item_cnt, first_item = map(int, input().split())
    last_item = first_item + item_cnt - 1
    taste = (2 * first_item + item_cnt - 1) * item_cnt // 2
    if first_item > 0:
        print(taste - first_item)
    elif last_item >= 0:
        print(taste)
    else:
        print(taste - last_item)


if __name__ == "__main__":
    main()
