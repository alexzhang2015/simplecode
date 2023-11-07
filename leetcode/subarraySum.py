# 2023.10.18

# 前缀和的思路是:
# 对于数组 nums[0..n-1],定义前缀和数组 preSum[0..n-1],其中:
# preSum[0] = nums[0]
# preSum[1] = nums[0] + nums[1]
# ...
# preSum[i] = nums[0] + nums[1] + ... + nums[i]
# 也就是说,preSum[i]表示 nums数组从下标0到i的元素之和。
# 这样一来,对于任意区间 nums[i..j] 的和就可以用 preSum[j] - preSum[i-1] 来表示。
# 利用这个性质,我们可以将区间求和问题转化为简单的前缀和计算。
# 例如在本题中,如果存在一个子数组 nums[i..j] 它的和为 k,那么根据前缀和性质,就有:
# preSum[j] - preSum[i-1] = k
# 也就是说,只要我们遍历每个位置,检查当前前缀和与 k 的关系,就可以解决这个问题。
# 综上,前缀和数组将区间求和转化为了单点求和,极大简化了过程,使我们能够在线性时间内解决这类区间问题。这就是前缀和技巧的关键所在。


class Solution:
    # https://leetcode.cn/problems/subarray-sum-equals-k/solutions/1447027/python3-by-wu-qiong-sheng-gao-de-qia-non-w6jw/?envType=study-plan-v2&envId=top-100-liked
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        preSum = 0
        hashMap = {0:1}
        
        for i in range(len(nums)):
            preSum += nums[i]
            if preSum-k in hashMap:
                count += hashMap[preSum-k]
            hashMap[preSum] = hashMap.get(preSum, 0) + 1
            print(preSum, k, hashMap)
        return count
    
    # 思路： 先遍历数组，将数字都存入到 HashSet 中便于在常量时间内找到值是否存在。然后再次遍历数组，当 set 中不存在 num-1 的时候，表示这是起点，然后寻找 num + 1， num + 2 ... num + k 是否存在，更新结果即可。
    # https://leetcode.cn/problems/longest-consecutive-sequence/
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        set_nums = set(nums)
        for num in nums:
            if num-1 not in set_nums:
                count = 0
                while num in set_nums:
                    count += 1
                    num += 1
                longest = max(longest, count)
        return longest
    


        
solution = Solution()
print (solution.subarraySum([2,2,0,3,0,4,5,6,2], 3))   