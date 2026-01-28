from solution import *

def test_example_1():
    h = create_my_hash_map()
    put(h, 1, 1)
    put(h, 2, 2)
    assert get(h, 1) == 1, "First get(1) should return 1"
    assert get(h, 3) == -1, "get(3) should return -1"
    put(h, 2, 1)
    assert get(h, 2) == 1, "After updating key 2, get(2) should return 1"
    remove(h, 2)
    assert get(h, 2) == -1, "After removal, get(2) should return -1"

def test_put_overwrite():
    h = create_my_hash_map()
    put(h, 1, 5)
    put(h, 1, 3)
    assert get(h, 1) == 3, "Overwriting key 1 should result in value 3"

def test_remove_key():
    h = create_my_hash_map()
    put(h, 5, 10)
    remove(h, 5)
    assert get(h, 5) == -1, "Removed key should return -1 when retrieved"

def test_multiple_operations():
    h = create_my_hash_map()
    put(h, 1, 10)
    put(h, 2, 20)
    assert get(h, 1) == 10, "Initial get(1) should return 10"
    assert get(h, 2) == 20, "Initial get(2) should return 20"
    put(h, 1, 15)
    assert get(h, 1) == 15, "Updating key 1 should set value to 15"