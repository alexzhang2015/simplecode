from typing import List
from typing import Optional

class Solution:
    
    # 其实回溯算法和我们常说的 DFS 算法非常类似，本质上就是一种暴力穷举算法。回溯算法和 DFS 算法的细微差别是：回溯算法是在遍历「树枝」，DFS 算法是在遍历「节点」，
    # 抽象地说，解决一个回溯问题，实际上就是遍历一棵决策树的过程，树的每个叶子节点存放着一个合法答案。你把整棵树遍历一遍，把叶子节点上的答案都收集起来，就能得到所有的合法答案。
    # 站在回溯树的一个节点上，你只需要思考 3 个问题：
    # 1、路径：也就是已经做出的选择。
    # 2、选择列表：也就是你当前可以做的选择。
    # 3、结束条件：也就是到达决策树底层，无法再做选择的条件。
    # 如果你不理解这三个词语的解释，没关系，我们后面会用「全排列」和「N 皇后问题」这两个经典的回溯算法问题来帮你理解这些词语是什么意思，现在你先留着印象。

    # 全排列：只要从根遍历这棵树，记录路径上的数字，其实就是所有的全排列。我们不妨把这棵树称为回溯算法的「决策树」。


    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        result = []
        self.generate_permutations(nums, [], result)
        return result
        
    def generate_permutations(self, nums: List[int], current_permutation: List[int], result: List[List[int]]):
        if not nums:
            result.append(current_permutation)
            return
        
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            new_permutation = current_permutation + [nums[i]]
            print(new_nums, current_permutation, new_permutation)
            self.generate_permutations(new_nums, new_permutation, result)
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)

solution = Solution()
print(solution.permute([1,2,3]))