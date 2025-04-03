#  Variant 1: number in group list (21) % 4 = 1

class ListNode:
    def __init__(self, data: str):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def append(self, element: str) -> None:
        new_node = ListNode(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")

        new_node = ListNode(element)
        if index == 0:
            if not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index == self.length:
            self.append(element)
            return
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
        self.length += 1

    def delete(self, index: int) -> str:
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")

        if index == 0:
            data = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.length - 1:
            data = self.tail.data
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            data = current.data
            current.prev.next = current.next
            current.next.prev = current.prev
        self.length -= 1
        return data


    def get(self, index: int) -> str:
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def reverse(self) -> None:
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head






