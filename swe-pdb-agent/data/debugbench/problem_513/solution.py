from typing import Dict

def my_hash_map_init() -> Dict[int, int]:
    return {}

def put(h: Dict[int, int], key: int, value: int) -> None:
    if key in h:
        h[key] = value + 1
    else:
        h[key] = value

def get(h: Dict[int, int], key: int) -> int:
    if key not in h:
        return -1
    else:
        return h[key]

def remove(h: Dict[int, int], key: int) -> None:
    if key in h:
        del h[key]