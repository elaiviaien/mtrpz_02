class DoublyLinkedList:
    def __init__(self):
        self._data = []

    def length(self) -> int:
        return len(self._data)

    def append(self, element: str) -> None:
        self._data.append(element)

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > len(self._data):
            raise IndexError("Index out of bounds")
        self._data.insert(index, element)

    def delete(self, index: int) -> str:
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of bounds")
        return self._data.pop(index)

    def delete_all(self, element: str) -> None:
        self._data = [item for item in self._data if item != element]

    def get(self, index: int) -> str:
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of bounds")
        return self._data[index]

    def clone(self) -> "DoublyLinkedList":
        new_list = DoublyLinkedList()
        new_list._data = self._data.copy()
        return new_list

    def reverse(self) -> None:
        self._data.reverse()

    def find_first(self, element: str) -> int:
        try:
            return self._data.index(element)
        except ValueError:
            return -1

    def find_last(self, element: str) -> int:
        for i in range(len(self._data) - 1, -1, -1):
            if self._data[i] == element:
                return i
        return -1

    def clear(self) -> None:
        self._data.clear()

    def extend(self, other: "DoublyLinkedList") -> None:
        self._data.extend(other._data)

if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append("A")
    dll.append("B")
    dll.append("C")
    print("After append:", dll._data)

    dll.insert("X", 1)
    print("After insert:", dll._data)

    deleted = dll.delete(2)
    print("Deleted element:", deleted)
    print("After delete:", dll._data)

    dll.delete_all("X")
    print("After delete_all:", dll._data)

    print("Element at index 1:", dll.get(1))

    cloned_dll = dll.clone()
    print("Cloned list:", cloned_dll._data)

    dll.reverse()
    print("After reverse:", dll._data)

    print("First occurrence of 'A':", dll.find_first("A"))

    print("Last occurrence of 'A':", dll.find_last("A"))

    dll.clear()
    print("After clear:", dll._data)

    dll.append("D")
    dll.append("E")

    other_dll = DoublyLinkedList()
    other_dll.append("F")
    other_dll.append("G")

    dll.extend(other_dll)
    print("After extend:", dll._data)

