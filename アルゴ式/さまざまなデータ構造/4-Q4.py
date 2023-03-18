class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.nxt = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def _is_empty(self) -> bool:
        return self.head is None

    def _append_first(self, node: Node) -> None:
        self.head = node
        self.tail = node

    def append(self, value):
        new_node = Node(value)
        if self._is_empty():
            self._append_first(new_node)
            return
        self.tail.nxt = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def appendleft(self, value):
        new_node = Node(value)
        if self._is_empty():
            self._append_first(new_node)
            return
        self.head.prev = new_node
        new_node.nxt = self.head
        self.head = new_node

    def pop(self):
        if self._is_empty():
            print("Error")
            return None
        ret = self.tail
        if self.tail.prev is None:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.nxt = None
        return ret

    def popleft(self):
        if self._is_empty():
            print("Error")
            return None
        ret = self.head
        if self.head.nxt is None:
            self.tail = self.head = None
        else:
            self.head = self.head.nxt
            self.head.prev = None
        return ret


def main():
    Q = int(input())
    linked = DoublyLinkedList()
    for _ in range(Q):
        n, *q = input().split()
        if n == "0":
            linked.appendleft(q[0])
        elif n == "1":
            linked.append(q[0])
        elif n == "2":
            d = linked.popleft()
            if d is not None:
                print(d.val)
        else:
            d = linked.pop()
            if d is not None:
                print(d.val)


if __name__ == "__main__":
    main()
