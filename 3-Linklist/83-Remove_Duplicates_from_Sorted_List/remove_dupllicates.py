class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       cur = head

       if head is None:
        return head
       else:

        while cur.next != None:
           if cur.val == cur.next.val:
              cur.next = cur.next.next
           else:
               cur = cur.next
        return head       

