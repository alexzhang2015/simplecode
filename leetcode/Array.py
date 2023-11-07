from typing import List
from typing import Optional

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        delete_idex = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                delete_idex.append(i)
        delete_idex.sort(reverse=True)
        for index in delete_idex:
            nums.pop(index)
        print(nums)    
    
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        result = ""
        for i in range(len(s)):
            result = max(self.palindrome(s, i, i), self.palindrome(s, i, i+1), result, key=len)
        return result
    
    # 在 s 中寻找以 s[l] 和 s[r] 为中心的最长回文串    # return result
    def palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    # https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
    # 默认排序方案
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        
        return []
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]

    # https://leetcode.cn/problems/two-sum
    # 不排序的方案
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

    # https://leetcode.cn/problems/move-zeroes/
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i - zero_count] = nums[i]
            else:
                zero_count += 1
        for i in range(len(nums) - zero_count, len(nums)):
            nums[i] = 0


    # https://leetcode.cn/problems/remove-element/
    # 注意：这里面nums是引用传值
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)
    
    # https://leetcode.cn/problems/reverse-string/
    # s.reverse()
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


    # https://leetcode.cn/problems/merge-intervals
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
    
    # https://leetcode.cn/problems/container-with-most-water/?envType=study-plan-v2&envId=top-100-liked
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        maxh = max(height)
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if max_area >= maxh * (right - left):
                break
        return max_area
    
    # https://leetcode.cn/problems/rotate-array/?envType=study-plan-v2&envId=top-100-liked
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the list in-place.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]
        
        # for i in range(k):
        #     nums.insert(0, nums.pop())
        
        
    # https://leetcode.cn/problems/group-anagrams/?envType=study-plan-v2&envId=top-100-liked
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            sortedStr = ''.join(sorted(s)) # 排序字符串
            if sortedStr in dic:
                dic[sortedStr].append(s)
            else:
                dic[sortedStr] = [s]
        
        return list(dic.values())
        
    # https://leetcode.cn/problems/3sum
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # dic = {num: i for i, num in enumerate(nums)}
        # 对nums进行排序，便于后续的双指针遍历
        nums.sort()
        res = []
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        # 规避[[0,0,0],[0,0,0]]结果，去重
        res_dict = {}
        for item in res:
            res_dict[tuple(item)] = None
        res = list(res_dict.keys())
        
        return res
            
        
        

solution = Solution()
solution.removeDuplicates([1,1,1,2])
print(solution.longestPalindrome("bdabad"))
print(solution.twoSum([2,7,11,15], 9))
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
print(solution.threeSum([-2,0,1,1,2]))