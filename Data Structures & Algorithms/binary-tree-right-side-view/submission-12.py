# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = deque()
        if root:
            level.append(root)
        right = []
        next_level = deque()
        while level:
            curr = level.popleft()
            if curr.left:
                next_level.append(curr.left)
            if curr.right:
                next_level.append(curr.right)
            if not level:
                right.append(curr.val)
                level = next_level
                next_level = deque()
        return right

        