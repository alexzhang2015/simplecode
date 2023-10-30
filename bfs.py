from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # 递归遍历
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        if left_depth == 0 or right_depth == 0:
            return left_depth + right_depth + 1
            
        return min(left_depth, right_depth) + 1
    
    # https://medium.com/nerd-for-tech/graph-traversal-in-python-bfs-dfs-dijkstra-a-star-parallel-comparision-dd4132ec323a
    # BFS 当遇到第一个叶子节点的时候，该节点深度就是最小深度。
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(1, root)]
        while queue:
            depth, node = queue.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((depth + 1, node.left))
            if node.right:
                queue.append((depth + 1, node.right))

    # DFS，需要把所有的叶子节点的深度进行比较，才可以得到最终的最小深度。
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        stack = [(1, root)]
        min_depth = float('inf')
        while stack:
            depth, node = stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
            if node.right:
                stack.append((depth + 1, node.right))
            if node.left:
                stack.append((depth + 1, node.left))       
        return min_depth 

    # https://leetcode.cn/problems/binary-tree-level-order-traversal/
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
