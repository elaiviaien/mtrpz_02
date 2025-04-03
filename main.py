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

    def _get_node_at(self, index: int) -> ListNode:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def _delete_node(self, node: ListNode) -> None:
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            node.next.prev = node.prev
        self._length -= 1
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

        if index == self._length:
            self.append(element)
        elif index == 0:
            new_node = ListNode(element)
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            self._length += 1
        else:
            current = self._get_node_at(index)
            new_node = ListNode(element)
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self._length += 1

    def delete(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")

        node_to_delete = self._get_node_at(index)
        data = node_to_delete.data

        self._delete_node(node_to_delete)
        return data

    def delete_all(self, element: str) -> None:
        current = self.head
        while current:
            next_node = current.next  # Save the next node
            if current.data == element:
                self._delete_node(current)
            current = next_node

    def get(self, index: int) -> str:
        return self._get_node_at(index).data

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
        if other.head is None:
            return
        if self.head is None:
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            other.head.prev = self.tail
            self.tail = other.tail
        self._length += other._length
