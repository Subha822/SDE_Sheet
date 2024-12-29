class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        def preorder(node, arr):
            if not node:
                return
            arr.append(node.val)
            preorder(node.left, arr)
            preorder(node.right, arr)
        arr = []
        preorder(root, arr)
        return arr