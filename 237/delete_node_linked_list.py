from uuid import RESERVED_FUTURE


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        if node.next is None:
            return

        node_next_next = node.next.next
        node.val = node.next.val
        node.next = node_next_next
