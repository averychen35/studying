# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head_1 = list1
        head_2 = list2
        if head_1.val < head_2.val:
            new_head = head_1
            curr = new_head
            head_1 = head_1.next
        else:
            new_head = head_2
            curr = new_head
            head_2 = head_2.next
        while head_1 and head_2:
            if head_1.val < head_2.val:
                curr.next = head_1
                head_1 = head_1.next
            else:
                curr.next = head_2
                head_2 = head_2.next
            curr = curr.next
        if head_2:
            curr.next = head_2
        if head_1:
            curr.next = head_1
        return new_head


        