class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.nxt = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.nxt = self.head
        self.head.prev = new_node
        self.head = new_node

    def pop(self):
        if self.tail is None:
            print("Error")
            return
        ret = self.tail
        if self.tail.prev is None:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
        return ret


def main():
    Q = int(input())
    linked = DoublyLinkedList()
    for _ in range(Q):
        n, *q = input().split()
        if n == "0":
            linked.insert(q[0])
        else:
            node = linked.pop()
            if node is not None:
                print(node.val)


if __name__ == "__main__":
    main()
