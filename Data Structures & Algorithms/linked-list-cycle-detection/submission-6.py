# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        fast, slow = head.next, head.next.next
        while fast != slow:
            if not fast.next:
                return False
            fast = fast.next
            if not slow or not slow.next:
                return False
            slow = slow.next.next
        return True


        