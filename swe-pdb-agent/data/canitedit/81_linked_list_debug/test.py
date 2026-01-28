from solution import *
import math

def test_all():
    def test_add_elements():
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        assert linked_list.head.value == 1, "Head should be 1"
        assert linked_list.head.next.value == 2, "Second element should be 2"

    def test_find_existing_element():
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        node = linked_list.find(2)
        assert node is not None and node.value == 2, "Should find element 2"

    def test_find_non_existing_element():
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        node = linked_list.find(3)
        assert node is None, "Should not find non-existing element"

    def test_delete_existing_element():
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        linked_list.delete(1)
        assert linked_list.head.value == 2, "Head should now be 2"

    def test_delete_non_existing_element():
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.delete(3)
        assert linked_list.head is not None and linked_list.head.value == 1, "List should remain unchanged"

    def test_list_integrity_after_deletions():
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)
        linked_list.delete(2)
        assert linked_list.head.value == 1 and linked_list.head.next.value == 3, "List should skip the deleted element"

    def run_tests():
        test_add_elements()
        test_find_existing_element()
        test_find_non_existing_element()
        test_delete_existing_element()
        test_delete_non_existing_element()
        test_list_integrity_after_deletions()
    run_tests()