class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.next = None
            self.prev = None
            self.key = key
            self.val = val

    def __init__(self, capacity: int):
        self.mapping = {}
        self.head = None
        self.tail = None
        self.cap = capacity

    def _bring_to_tail(self, node:Node):
        if self.tail == node:
            return

        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            return
        
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        if self.head == node:
            self.head = node.next
        
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def get(self, key: int) -> int:
        if not key in self.mapping:
            print("GET", key, "=", -1)
            return -1
        
        res = self.mapping[key]
        self._bring_to_tail(res)
        print("GET", key,"=", res.val)
        return res.val
        
    
    def put(self, key: int, value: int) -> None:
        curr_node = None
        if key in self.mapping:
            curr_node = self.mapping[key]
            curr_node.val = value
        else:
            curr_node = self.Node(key, value)
            self.mapping[key] = curr_node

        self._bring_to_tail(curr_node)

        if len(self.mapping) > self.cap:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del self.mapping[temp.key]
        
        print("PUT", key, value, self.head.key, self.tail.key)


        
        

        

        
