# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        cur = result

        carry = 0
        while True:

            part = 0

            if l1 is not None:
                part += l1.val
            if l2 is not None:
                part += l2.val
            part += carry
            
            cur.val = part % 10

            q = part // 10
            carry = q

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            if l1 is None and l2 is None and carry == 0:
                break
            
            new_node = ListNode()
            cur.next = new_node
            cur = new_node

        return result