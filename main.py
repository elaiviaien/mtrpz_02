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
        self._length = 0

    def length(self):
        return self._length

    def append(self, element: str) -> None:
        new_node = ListNode(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._length += 1

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self._length:
            raise IndexError("Index out of bounds")

        new_node = ListNode(element)
        if index == 0:
            if not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index == self._length:
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
        self._length += 1

    def delete(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")

        if index == 0:
            data = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self._length - 1:
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
        self._length -= 1
        return data

    def delete_all(self, element: str) -> None:
        current = self.head
        while current:
            if current.data == element:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self._length -= 1
            current = current.next

    def get(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def clone(self) -> "DoublyLinkedList":
        new_list = DoublyLinkedList()
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list

    def reverse(self) -> None:
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head

    def find_first(self, element: str) -> int:
        current = self.head
        index = 0
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1

    def find_last(self, element: str) -> int:
        current = self.tail
        index = self._length - 1
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self) -> None:
        self.head = self.tail = None
        self._length = 0

    def extend(self, other: "DoublyLinkedList") -> None:
        if not other.head:
            return
        if not self.head:
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            other.head.prev = self.tail
            self.tail = other.tail
        self._length += other._length
