from solution import *
import math

def test_all():
    def test_cache_statistics():
        cache = KeyValueCache()

        assert cache.get_hits() == 0, "Hits initialization failed"
        assert cache.get_misses() == 0, "Misses initialization failed"
        assert cache.get_num_entries() == 0, "Entries initialization failed"

        cache.put("key1", "value1")
        cache.get_by_primary("key1")
        cache.get_by_primary("key2")
        assert cache.get_hits() == 1, "Hits stats failed"
        assert cache.get_misses() == 1, "Misses stats failed"
        assert cache.get_num_entries() == 1, "Entries stats failed"

        cache.put("key2", "value2", ["skey1"])
        assert cache.get_hits() == 1, "Hits stats failed after adding and deleting"
        assert cache.get_misses() == 1, "Misses stats failed after adding and deleting"
        assert cache.get_num_entries() == 2, "Entries stats failed after adding and deleting"
        
        cache.delete("key1")
        assert cache.get_hits() == 1, "Hits stats failed after adding and deleting"
        assert cache.get_misses() == 1, "Misses stats failed after adding and deleting"
        assert cache.get_num_entries() == 1, "Entries stats failed after adding and deleting"

    def test_put_and_get_primary():
        cache = KeyValueCache()
        cache.put("key1", "value1")
        assert cache.get_by_primary("key1") == "value1", "Failed to get value by primary key"

    def test_put_and_get_secondary():
        cache = KeyValueCache()
        cache.put("key1", "value1", ["skey1", "skey2"])
        assert cache.get_by_secondary("skey1") == "value1", "Failed to get value by first secondary key"
        assert cache.get_by_secondary("skey2") == "value1", "Failed to get value by second secondary key"

    def test_update_primary_key():
        cache = KeyValueCache()
        cache.put("key1", "value1")
        cache.put("key1", "value2")
        assert cache.get_by_primary("key1") == "value2", "Failed to update value by primary key"

    def test_delete_primary_key():
        cache = KeyValueCache()
        cache.put("key1", "value1", ["skey1"])
        cache.delete("key1")
        assert cache.get_by_primary("key1") is None, "Failed to delete value by primary key"
        assert cache.get_by_secondary("skey1") is None, "Secondary key should also return None after primary key deletion"

    def test_secondary_key_unique_to_primary():
        cache = KeyValueCache()
        cache.put("key1", "value1", ["skey"])
        cache.put("key2", "value2", ["skey"])
        assert cache.get_by_secondary("skey") == "value2", "Secondary key should map to the most recently associated primary key"

    def test_no_secondary_key():
        cache = KeyValueCache()
        cache.put("key1", "value1")
        assert cache.get_by_secondary("skey1") is None, "Should return None for non-existent secondary key"

    test_put_and_get_primary()
    test_put_and_get_secondary()
    test_update_primary_key()
    test_delete_primary_key()
    test_secondary_key_unique_to_primary()
    test_no_secondary_key()
    test_cache_statistics()