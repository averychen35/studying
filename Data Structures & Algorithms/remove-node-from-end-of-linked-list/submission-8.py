# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # maintain a gap of n between two pointers, when the further one's next gets to 
        # null, that is the one we want to remove
        dummy = ListNode()
        dummy.next = head
        first = head
        for i in range(n):
            first = first.next
        second = dummy
        while first:
            second = second.next
            first = first.next
        
        second.next = second.next.next

        return dummy.next

        