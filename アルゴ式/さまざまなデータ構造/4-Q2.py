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

    def remove_start(self) -> None:
        """先頭要素を削除する"""
        self.head = self.head.nxt

    def output(self) -> None:
        """k番目から出力する"""
        if self.head is None:
            print("Error")
            return
        print(self.head.val)
        self.remove_start()


def main():
    Q = int(input())
    linked = LinkedList()
    for _ in range(Q):
        n, *q = input().split()
        if n == "0":
            linked.insert_start(q[0])
        else:
            linked.output()


if __name__ == "__main__":
    main()
