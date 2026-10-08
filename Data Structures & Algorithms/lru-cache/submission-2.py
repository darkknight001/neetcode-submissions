class ListNode:
    def __init__(self, key, val, next_node=None, prev_node=None):
        self.val = val
        self.key = key
        self.next = next_node
        self.prev = prev_node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.memory = {}
        # sentinel nodes: head.next is most-recently-used, tail.prev is least-recently-used
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def print_cache(self):
        ans = []
        node = self.head.next
        while node is not self.tail:
            ans.append(node.val)
            node = node.next
        print(ans)

    def _remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: ListNode) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.memory:
            return -1

        node = self.memory[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.memory:
            node = self.memory[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
            return

        if len(self.memory) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.memory[lru.key]

        node = ListNode(key, value)
        self.memory[key] = node
        self._add_to_front(node)
