import pytest
from ..main import DoublyLinkedList, ListNode


@pytest.fixture
def empty_list():
    return DoublyLinkedList()


@pytest.fixture
def sample_list():
    lst = DoublyLinkedList()
    lst.append("a")
    lst.append("b")
    lst.append("c")
    return lst


def test_length(empty_list, sample_list):
    assert empty_list.length() == 0
    assert sample_list.length() == 3


def test_append(empty_list):
    empty_list.append("a")
    assert empty_list.length() == 1
    assert empty_list.get(0) == "a"


def test_insert(empty_list, sample_list):
    empty_list.insert("a", 0)
    assert empty_list.length() == 1
    assert empty_list.get(0) == "a"

    sample_list.insert("x", 1)
    assert sample_list.length() == 4
    assert sample_list.get(1) == "x"
    assert sample_list.get(2) == "b"


def test_delete(empty_list, sample_list):
    deleted_data = sample_list.delete(1)
    assert deleted_data == "b"
    assert sample_list.length() == 2
    assert sample_list.get(1) == "c"

    with pytest.raises(IndexError):
        empty_list.delete(0)

    deleted_data = sample_list.delete(0)
    assert deleted_data == "a"
    assert sample_list.length() == 1


def test_delete_all(sample_list):
    sample_list.delete_all("a")
    assert sample_list.length() == 2

    sample_list.delete_all("c")
    assert sample_list.length() == 1

    sample_list.delete_all("x")
    assert sample_list.length() == 1


def test_get(empty_list, sample_list):
    with pytest.raises(IndexError):
        empty_list.get(0)

    assert sample_list.get(0) == "a"
    assert sample_list.get(1) == "b"
    assert sample_list.get(2) == "c"


def test_clone(sample_list):
    cloned_list = sample_list.clone()
    assert cloned_list.length() == sample_list.length()
    assert cloned_list.get(0) == sample_list.get(0)
    assert cloned_list.get(1) == sample_list.get(1)
    assert cloned_list.get(2) == sample_list.get(2)


def test_reverse(sample_list):
    sample_list.reverse()
    assert sample_list.get(0) == "c"
    assert sample_list.get(1) == "b"
    assert sample_list.get(2) == "a"


def test_find_first(sample_list):
    assert sample_list.find_first("a") == 0
    assert sample_list.find_first("b") == 1
    assert sample_list.find_first("x") == -1


def test_find_last(sample_list):
    assert sample_list.find_last("a") == 0
    assert sample_list.find_last("b") == 1
    assert sample_list.find_last("c") == 2
    assert sample_list.find_last("x") == -1


def test_clear(sample_list):
    sample_list.clear()
    assert sample_list.length() == 0


def test_extend(sample_list):
    other_list = DoublyLinkedList()
    other_list.append("d")
    other_list.append("e")

    sample_list.extend(other_list)
    assert sample_list.length() == 5
    assert sample_list.get(3) == "d"
    assert sample_list.get(4) == "e"

    empty_list = DoublyLinkedList()
    empty_list.extend(sample_list)
    assert empty_list.length() == 5

def test_insert_at_middle(sample_list):
    sample_list.insert("x", 1)
    assert sample_list.length() == 4
    assert sample_list.get(1) == "x"
    assert sample_list.get(2) == "b"


def test_insert_at_end(sample_list):
    sample_list.insert("z", sample_list.length())
    assert sample_list.length() == 4
    assert sample_list.get(3) == "z"


def test_insert_at_beginning(sample_list):
    sample_list.insert("y", 0)
    assert sample_list.length() == 4
    assert sample_list.get(0) == "y"


def test_delete_last_element(sample_list):
    deleted_data = sample_list.delete(sample_list.length() - 1)
    assert deleted_data == "c"
    assert sample_list.length() == 2
    assert sample_list.get(1) == "b"


def test_delete_first_element(sample_list):
    deleted_data = sample_list.delete(0)
    assert deleted_data == "a"
    assert sample_list.length() == 2
    assert sample_list.get(0) == "b"


def test_delete_middle_element(sample_list):
    deleted_data = sample_list.delete(1)
    assert deleted_data == "b"
    assert sample_list.length() == 2
    assert sample_list.get(0) == "a"
    assert sample_list.get(1) == "c"


def test_delete_out_of_bounds():
    sample_list = DoublyLinkedList()
    sample_list.append("a")
    sample_list.append("b")

    with pytest.raises(IndexError):
        sample_list.delete(2)


def test_insert_out_of_bounds():
    sample_list = DoublyLinkedList()
    sample_list.append("a")

    with pytest.raises(IndexError):
        sample_list.insert("b", 2)


def test_find_first_empty_list():
    empty_list = DoublyLinkedList()
    assert empty_list.find_first("a") == -1


def test_find_last_empty_list():
    empty_list = DoublyLinkedList()
    assert empty_list.find_last("a") == -1


def test_extend_empty_list():
    empty_list = DoublyLinkedList()
    another_list = DoublyLinkedList()
    another_list.append("a")

    empty_list.extend(another_list)
    assert empty_list.length() == 1
    assert empty_list.get(0) == "a"


def test_reverse_empty_list():
    empty_list = DoublyLinkedList()
    empty_list.reverse()
    assert empty_list.length() == 0


def test_reverse_single_element_list():
    single_element_list = DoublyLinkedList()
    single_element_list.append("a")
    single_element_list.reverse()
    assert single_element_list.get(0) == "a"


def test_clone_empty_list():
    empty_list = DoublyLinkedList()
    cloned_list = empty_list.clone()
    assert cloned_list.length() == 0


def test_delete_all_no_occurrence():
    sample_list = DoublyLinkedList()
    sample_list.append("a")
    sample_list.append("b")
    sample_list.append("c")

    sample_list.delete_all("z")
    assert sample_list.length() == 3


def test_find_first_with_duplicates():
    sample_list = DoublyLinkedList()
    sample_list.append("a")
    sample_list.append("b")
    sample_list.append("a")

    assert sample_list.find_first("a") == 0
    assert sample_list.find_last("a") == 2


def test_find_last_with_duplicates():
    sample_list = DoublyLinkedList()
    sample_list.append("a")
    sample_list.append("b")
    sample_list.append("a")

    assert sample_list.find_first("b") == 1
    assert sample_list.find_last("b") == 1


def test_clear_empty_list():
    empty_list = DoublyLinkedList()
    empty_list.clear()
    assert empty_list.length() == 0
    assert empty_list.head is None
    assert empty_list.tail is None


def test_extend_with_empty_list():
    sample_list = DoublyLinkedList()
    sample_list.append("a")
    sample_list.append("b")

    empty_list = DoublyLinkedList()
    sample_list.extend(empty_list)
    assert sample_list.length() == 2


def test_append_same_element():
    sample_list = DoublyLinkedList()
    sample_list.append("a")
    sample_list.append("a")
    assert sample_list.length() == 2
    assert sample_list.get(0) == "a"
    assert sample_list.get(1) == "a"


def test_clone_with_same_data():
    sample_list = DoublyLinkedList()
    sample_list.append("a")
    sample_list.append("b")

    cloned_list = sample_list.clone()
    assert cloned_list.length() == sample_list.length()
    assert cloned_list.get(0) == sample_list.get(0)
    assert cloned_list.get(1) == sample_list.get(1)

if __name__ == "__main__":
    pytest.main()
