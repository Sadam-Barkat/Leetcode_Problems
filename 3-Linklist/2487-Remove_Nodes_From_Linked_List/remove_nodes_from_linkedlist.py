class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head
        while cur:
            while stack and stack[-1] < cur.val:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next


        dummy = ListNode()
        cur = dummy
        for val in stack:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next     