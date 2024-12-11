# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def gain(node, max_val):
            if not node:
                return 0

            if node.val >= max_val:
                count = 1
            else:
                count = 0   
            
            max_val = max(max_val, node.val)

            count = count + gain(node.left, max_val)    
            count = count + gain(node.right, max_val) 
            return count

        return gain(root, root.val)           
        