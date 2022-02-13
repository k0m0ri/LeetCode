# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymmetricHelper(left: TreeNode, right: TreeNode) -> bool:
            # base case: if both are null, return True
            if left is None and right is None:
                return True

            # asymmetric leaf, return False
            # corner case
            #    2         null
            # if left or right is null, then return false
            if left is None or right is None:
                return False

            # left.val and right.val is already checked to be the same
            # corner case
            #    2                2
            #   /.\              /. \
            #  3   null       null  null

            # corner case
            #    2                2
            #   /.\              /. \
            # null  3           3  null
            # left.val and right.val is already checked to be the same

            # check if left.left == right.right, if not False
            if left.left is not None and right.right is not None and left.left.val != right.right.val:
                return False

            # check if left.right == right.left, if not False
            if left.right is not None and right.left is not None and left.right.val != right.left.val:
                return False

            # recurse here isSymmetricHelper(left.left, right.right)
            return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)

        # corner case: if root is null, return True
        if root is None:
            return True

        # testcase1: [1,2,2,3,4,4,3]
        # case
        #    1
        # if left AND right subtree null, return true
        if root.left is None and root.right is None:
            return True

        # case when asymmetric
        # case
        #    1
        #   /
        #  2
        # if left or right subtrees is null, return false
        if root.left is None or root.right is None:
            return False

        # level 1's child nodes must be same, otherwise return False
        # case
        #    1
        #   /.\
        #  2   3
        # if root's left and root's right is not same return false
        if root.left.val != root.right.val:
            return False

        # case
        #    1
        #   /.\
        #  2   2
        return isSymmetricHelper(root.left, root.right)
