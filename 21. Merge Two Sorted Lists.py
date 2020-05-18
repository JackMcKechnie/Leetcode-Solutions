# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        out_head = ListNode()
        out = out_head

        if l1 == None and l2 == None:
            return None

        if l1 == None:
            return l2

        if l2 == None:
            return l1

        while l1 != None and l2 != None:

            if l1.val < l2.val:
                print(l1.val)
                out.val = l1.val
                out.next = ListNode()
                out = out.next
                l1 = l1.next
                continue

            if l2.val < l1.val:
                print(l2.val)
                out.val = l2.val
                out.next = ListNode()
                out = out.next
                l2 = l2.next
                continue

            if l1.val == l2.val:
                print(l1.val)
                for i in range(2):
                    out.val = l1.val
                    out.next = ListNode()
                    out = out.next
                l1 = l1.next
                l2 = l2.next

        if l1 == None:
            while l2 != None:
                print(l2.val)
                out.val = l2.val
                out.next = ListNode()
                out = out.next
                l2 = l2.next

        if l2 == None:
            while l1 != None:
                print(l1.val)
                out.val = l1.val
                out.next = ListNode()
                out = out.next
                l1 = l1.next

        out = out_head
        while out.next.next != None:
            print(out)
            out = out.next
        out.next = None

        print("")
        print(out_head)
        return out_head




