# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = l1
        list2 = l2
        Sum = 0
        carry = 0
        dummy = ListNode()
        cur = dummy

        while list1 or list2 or carry:
            first_digit = list1.val if list1 else 0
            second_digit = list2.val if list2 else 0
            Sum = first_digit + second_digit + carry
            carry = Sum // 10
            Sum = Sum % 10
            cur.next = ListNode(Sum)
            cur = cur.next
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        return dummy.next    
