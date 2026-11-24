# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
           return False

    # 2. Leaf check: If there are no left or right children,
    # check if the remaining target_sum equals this leaf's value
        if not root.left and not root.right:
            return targetSum == root.val

    # 3. Recursive step: Subtract current value and check left OR right
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)

            
            
        
        