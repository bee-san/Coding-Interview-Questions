# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        rootEnds = {}
        for counter, i in enumerate(root):
            if root[counter] + 1 == None or counter == len(root):
                rootEnds[i, counter]
