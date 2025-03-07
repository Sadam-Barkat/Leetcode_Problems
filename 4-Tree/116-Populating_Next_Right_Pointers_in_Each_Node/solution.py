"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = deque()
        q.append(root)

        while q:
            q2 = deque()

            for i in range(len(q)):
                cur = q.popleft()

                q2.append(cur)

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)

            while len(q2) > 1:
                cur = q2.popleft()
                cur.next = q2[0]

            cur = q2.popleft()
            cur.next = None

        return root