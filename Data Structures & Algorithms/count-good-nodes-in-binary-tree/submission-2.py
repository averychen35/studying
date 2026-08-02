# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if node:
                curr = 1 if node.val >= maxVal else 0
                return curr + dfs(node.left, max(maxVal, node.val)) + dfs(node.right, max(maxVal, node.val))
            else:
                return 0


        
        return dfs(root, float("-inf"))

        