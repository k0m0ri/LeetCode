from torch import ne


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        # cornercase: if head or head.next == None, return head
        if head is None or head.next is None:
            return head

        prev = None
        curr = head
        next = head.next
        while curr is not None:
            curr.next = prev

            prev = curr
            curr = next
            if next is not None:
                next = next.next
        
        head = prev
        return head
        