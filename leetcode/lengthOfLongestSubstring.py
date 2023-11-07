class Solution:
    # https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/?envType=study-plan-v2&envId=top-100-liked
    # 滑动窗口
    # 什么是滑动窗口？
    # 其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        start = 0
        
        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            longest = max(longest, i - start + 1)
            seen[char] = i
        
        return longest
              
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))