class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def sameTree(self,l,r):
        if not l and not r:
            return True
        if l and r and l.val == r.val:
            return self.sameTree(l.left,r.left) and self.sameTree(l.right,r.right)
        return False