class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 1
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))