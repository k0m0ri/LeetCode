class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():

    def middleNode(self, head):

        # cornercase: if head or head.next is null, return head
        if head is None or head.next is None:
            return head

        slow = head
        fast = head
        while fast.next is not None and fast.next.nextis is not None:
            slow = slow.next
            fast = fast.next.next

        middle = head
        # odd case
        if fast.next is None:
            middle = slow
        # even case
        else:
            middle = slow.next

        return middle
