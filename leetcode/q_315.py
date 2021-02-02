# Definition for a binary tree node.
## first try -> wrong 
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.maximum = float('-inf')

        def dfs(root):
            if root == None:
                return 0
            left_max = max(0,dfs(root.left))
            right_max = max(0,dfs(root.right))
            self.maximum = max(self.maximum, left_max + right_max + root.val)

            return max(left_max,right_max)+root.val
        dfs(root)
        return self.maximum

## second solution
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root in None:
            return 0
        self.s = 0
        self.sum(root)
        return self.s
    def sum(self,root):
        if root is None:
            return 
        if root.val%2 ==0:
            if root.left:
                if root.left.lef:
                    self.s+=root.left.left.val
                if root.left.right:
                    self.s+=root.left.right.val
            if root.right:
                if root.right.left:
                    self.s+=root.right.left.val
                if root.right.right:
                    self.s+=root.right.right.val
        self.sum(root.left)
        self.sum(root.right)



