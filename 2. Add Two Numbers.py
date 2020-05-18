# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Get value of 1st number from l1
        n1_str = ""
        while (l1 != None):
            n1_str += str(l1.val)
            l1 = l1.next

        # Get value of 2nd number from l2
        n2_str = ""
        while (l2 != None):
            n2_str += str(l2.val)
            l2 = l2.next

        # Reverse numbers and save as ints
        n1 = int(n1_str[::-1])
        n2 = int(n2_str[::-1])

        out_num = n1 + n2

        # Reverse and save as string
        out_str = str(out_num)[::-1]

        out_ll = ListNode()

        # Populate linked list
        head = out_ll
        for i in range(len(out_str)):
            head.val = out_str[i]
            if (i != len(out_str) - 1):
                head.next = ListNode()
                head = head.next

        return (out_ll)


