from typing import List
from typing import Optional

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

    # https://leetcode.cn/problems/invert-binary-tree/
    # 二叉树反转，指针赋值+递归
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return
        if root.left or root.right:
            tmp = root.right
            root.right = root.left
            root.left = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
    
    # https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
    def preorder(self, node: Optional[TreeNode], pre: []):
        if node:
            pre.append(node.val)
            self.preorder(node.left, pre)
            self.preorder(node.right, pre)
    def flatten(self, root: Optional[TreeNode]) -> None:
        # 1. 前序遍历val
        pre = []
        self.preorder(root, pre)
        if not pre: return None 
        
        # 2. 用前序遍历的值，构建二叉树，将二叉树展开为链表
        p = root
        for i in pre[1:]:
            p.left = None
            p.right = TreeNode(i)
            p = p.right

    # https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/
    # 主函数 填充每个节点的下一个右侧节点指针
    def connect(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]':
        if root is None:
            return None
        # 遍历「三叉树」，连接相邻节点
        self.traverse(root.left, root.right)
        return root
    # 三叉树遍历框架
    def traverse(self, node1: 'Optional[TreeNode]', node2: 'Optional[TreeNode]'):
        if node1 is None or node2 is None:
            return
        # /**** 前序位置 ****/
        # 将传入的两个节点穿起来
        node1.next = node2

        # 连接相同父节点的两个子节点
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        # 连接跨越父节点的两个子节点
        self.traverse(node1.right, node2.left)    
        
    # https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/2361558/105-cong-qian-xu-yu-zhong-xu-bian-li-xu-4lvkz/
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root, left, right):
            if left > right: return                               # 递归终止
            node = TreeNode(preorder[root])                       # 建立根节点
            i = dic[preorder[root]]                               # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)              # 开启左子树递归
            node.right = recur(i - left + root + 1, i + 1, right) # 开启右子树递归
            return node                                           # 回溯返回根节点

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)

