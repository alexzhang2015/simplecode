class Solution:
    # https://leetcode.cn/problems/maximum-subarray/submissions/476166817/?envType=study-plan-v2&envId=top-100-liked
    # 总结：这是一道典型的使用「动态规划」解决的问题，需要我们掌握动态规划问题设计状态的技巧（无后效性），并且需要知道如何推导状态转移方程，最后再去优化空间。
    # dp[i] = Math.max(nums[i], nums[i] + dp[i - 1]);

    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum
    
