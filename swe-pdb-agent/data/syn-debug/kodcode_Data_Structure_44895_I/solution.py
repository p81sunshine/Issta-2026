class CircularBuffer:
    def __init__(self, size: int):
        self.buffer = [None] * size
        self.size_limit = size
        self.start = 0
        self.end = 0
        self.count = 0

    def put(self, item):
        self.buffer[self.end] = item
        self.end = (self.end + 1) % self.size_limit
        if self.count < self.size_limit:
            self.count += 1
        else:
            self.start = (self.start + 1) % self.size_limit

    def get(self, index: int):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")
        return self.buffer[self.start + index]

    def size(self) -> int:
        return self.count

    def full(self) -> bool:
        return self.count == self.size_limit

    def empty(self) -> bool:
        return self.count == 0