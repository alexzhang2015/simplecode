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
    
    # 在 s 中寻找以 s[l] 和 s[r] 为中心的最长回文串    # return result
    def palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    

solution = Solution()
solution.removeDuplicates([1,1,1,2])
print(solution.longestPalindrome("bdabad"))