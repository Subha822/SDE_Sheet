class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
class Solution(object):
    def middleNode(self,head):
        slow = head
        fast = head
        while fast and fast.next and slow:
            fast = fast.next.next 
            slow = slow.next
        return slow 