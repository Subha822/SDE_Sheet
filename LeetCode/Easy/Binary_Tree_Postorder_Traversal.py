class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        def postorder(node, arr):
            if not node:
                return
            postorder(node.left, arr)
            postorder(node.right, arr)
            arr.append(node.val)
        arr = []
        postorder(root, arr)
        return arr