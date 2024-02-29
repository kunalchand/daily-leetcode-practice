class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"


class LRUCache:

    def printList(self):
        cur = self.new

        while cur:
            print(cur, end=" ")
            cur = cur.right

        print("")

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.new = Node("new", "new")
        self.old = Node("old", "old")

        self.new.right = self.old
        self.old.left = self.new

    def remove(self, node: "Node") -> None:
        leftNode = node.left
        rightNode = node.right

        leftNode.right = rightNode
        rightNode.left = leftNode

    def add(self, node: "Node") -> None:
        newDummy = self.new
        rightOfNewDummy = newDummy.right

        newDummy.right = node

        node.left = newDummy
        node.right = rightOfNewDummy

        rightOfNewDummy.left = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.size += 1
            if self.size > self.capacity:
                self.cache.pop(self.old.left.key)
                self.remove(self.old.left)

            self.cache[key] = Node(key, value)
            self.add(self.cache[key])

        else:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.add(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
