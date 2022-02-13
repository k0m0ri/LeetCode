import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        
        max_depth_left = self.maxDepth(root.left)

        max_depth_right = self.maxDepth(root.right)

        return max(max_depth_left, max_depth_right) + 1
        