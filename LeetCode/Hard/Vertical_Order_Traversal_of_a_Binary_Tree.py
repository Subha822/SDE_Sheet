# Optimal Approach

from collections import deque, defaultdict

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        nodes = defaultdict(lambda: defaultdict(list))
        todo = deque([(root, (0, 0))])
        while todo:
            temp, (x, y) = todo.popleft()
            nodes[x][y].append(temp.val)
            if temp.left:
                todo.append((temp.left, (x - 1, y + 1)))
            if temp.right:
                todo.append((temp.right, (x + 1, y + 1)))
        ans = []
        for x in sorted(nodes.keys()):
            col = []
            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))
            ans.append(col)
        return ans