from datalist import Datalist

class LinkedList:
    def remove_tail(self):
        if self.is_empty():
            return None
        current = self.head
        while current.next.next:
            current = current.next
        removed_node = current.next
        current.next = None
        return removed_node

class LruCache(Datalist):
    def __init__(self, capacity=10):
        super().__init__()
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")
        self.capacity = capacity
        self.size = 0

    def add(self, data):
        if self.remove(data):
            self.size -= 1
        super().add_to_head(data)
        self.size += 1
        while self.size > self.capacity:
            removed_node = self.remove_tail()
            if removed_node:
                self.size -= 1

    def search(self, data):
        prev = self.head
        current = prev.next
        found = False
        while current:
            if current.data == data:
                found = True
                break
            prev = current
            current = current.next
        if not found:
            raise KeyError(f"Data {data} not found in cache")
        prev.remove_after()
        self.head.insert_after(current)
        return current.data