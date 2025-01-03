class TreeNode(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new_head