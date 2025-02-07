# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        arr = []

        def inorder(root):
            if not root:
                return 
            else:
                inorder(root.left) 
                arr.append(root.val)  
                inorder(root.right) 
                return arr

        inorder(root) 
        arr = list(set(arr))
        arr.sort()
        if len(arr) == 1:
            return -1
        else:    
            return arr[1]