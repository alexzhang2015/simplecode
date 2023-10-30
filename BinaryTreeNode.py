class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 前序遍历 
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# 中序遍历
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# 后序遍历        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# 示例树
root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')

# 前序遍历结果:A B D E C 
preorder(root) 

# 中序遍历结果:D B E A C
inorder(root)

# 后序遍历结果:D E B C A
postorder(root)

from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            depth = max(left_depth, right_depth) + 1
        return depth
    
def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
        
    left_depth = self.minDepth(root.left)
    right_depth = self.minDepth(root.right)
    
    if left_depth == 0 or right_depth == 0:
        return left_depth + right_depth + 1
        
    return min(left_depth, right_depth) + 1
