# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #   Add every linked list pair with the
    #   previous carry out and return sum and new
    #   carry out. Save sum as a new linked list
    #   node
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = return_res = ListNode()
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l1 = l1.next if l1 else None
            l2_val = l2.val if l2 else 0
            l2 = l2.next if l2 else None

            carry, rem = divmod(l1_val + l2_val + carry, 10)

            res.next = ListNode(rem)
            res = res.next

        return return_res.next
