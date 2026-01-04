class DoubleLinkedList:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None
        self.prev = None



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.map = {}
        self.node_map = {}
        

    def move_node_to_last(self, node: Optional[DoubleLinkedList]):
        if self.size == 1 or self.tail == node:
            return node.val

        if self.head == node:
            self.head = node.next
            self.head.prev = None
        else:
            # print('self.size: ', self.size, ', node.val : ', node.val)
            node.prev.next = node.next
            node.next.prev = node.prev
            
        
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        # move mode to end
        self.move_node_to_last(node = self.map[key])

        return self.map[key].val
        

    def put(self, key: int, value: int) -> None:
        # print('self.size: ', self.size, ', key : ', key)
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.move_node_to_last(node = node)
            return
        new_node = DoubleLinkedList(value)
        self.node_map[new_node] = key
        if self.size >= self.capacity:
            del self.map[self.node_map[self.head]]
            if self.size == 1:
                self.head = self.tail = new_node
                self.map[key] = new_node
                return

            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
            
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            if not self.head:
                self.head = new_node
                self.tail = self.head
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            self.size += 1
        
        self.map[key] = new_node


        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)