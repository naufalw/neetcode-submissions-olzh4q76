class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None

        self.values = {}

    def get(self, key: int) -> int:
        node = self.values.get(key)

        if node:
            self._move_to_tail(node)
            return node.val
        
        return -1

    def _move_to_tail(self, node):
        if self.tail == node:
            return

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        if self.head == node:
            self.head = node.next
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        node.next = None
        

    def put(self, key: int, value: int) -> None:
        node = self.values.get(key)
        if node:
            node.val = value
        else:
            node = Node(key, value)
        
        if not self.tail and not self.head:
            self.head = node
            self.tail = node
            self.values[key] = node
            return
        
        self._move_to_tail(node)
        self.values[key] = node

        if len(self.values) > self.capacity:
            head = self.head
            del self.values[head.key]
            if head.next:
                self.head = head.next
            self.head.prev = None

        
        
