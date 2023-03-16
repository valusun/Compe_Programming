class Node:
    def __init__(self, value):
        self.val = value
        self.nxt = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, value: str) -> None:
        """先頭に要素を挿入する"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        new_node.nxt = self.head
        self.head = new_node

    def output(self, k: int) -> None:
        """k番目まで出力する"""
        current = self.head
        cnt = 0
        output_data = []
        while current is not None and cnt <= k:
            output_data.append(current.val)
            current = current.nxt
            cnt += 1
        print(*output_data)


def main():
    Q = int(input())
    linked = LinkedList()
    for _ in range(Q):
        n, d = input().split()
        if n == "0":
            linked.insert_start(d)
        else:
            linked.output(int(d) - 1)


if __name__ == "__main__":
    main()
