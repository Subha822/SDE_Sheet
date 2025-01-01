from Queue import Queue
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        q = Queue()
        level = 0
        q.put(root)
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                front = q.get()
                if front.left is not None:
                    q.put(front.left)
                if front.right is not None:
                    q.put(front.right)
            level += 1
        return level