from curses import noecho
from tkinter.tix import Tree


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):

        # corner case: if head or head.next is None, return
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
