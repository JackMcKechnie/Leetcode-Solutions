# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        p2 = head
        for i in range(n):
            p2 = p2.next

        out_head = ListNode()
        out_working = out_head

        while p2 != None:
            out_working.next = ListNode()
            out_working = out_working.next
            out_working.val = p1.val
            p1 = p1.next
            p2 = p2.next

        p1 = p1.next

        while p1 != None:
            out_working.next = ListNode()
            out_working = out_working.next
            out_working.val = p1.val
            p1 = p1.next

        return out_head.next


