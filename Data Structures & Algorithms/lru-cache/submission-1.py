class Node:
    def __init__(self, key, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
  

    def __init__(self, capacity: int):
        self.values = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        node = self.values.get(key, None)

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
        node.next = None
        self.tail = node

        

    def put(self, key: int, value: int) -> None:
        node = self.values.get(key, None)

        if node:
            node.val = value
        else:
            node = Node(key, value)

        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            self.values[key] = node
            return
        
        self._move_to_tail(node)
        
        self.values[key] = node

        print("PUT", key, value, len(self.values), self.values)
        
        if len(self.values) > self.capacity:
            head = self.head
            del self.values[head.key]
            if head.next:
                head.next.prev = None
            self.head = head.next

        print("     PUT", key, value, len(self.values), self.values)
        
        


        
