class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = {}  # Stores the most recent index of each character
        start = 0  # Start index of the current substring
        longest = 0  # Length of the longest substring

        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                print("if", i, char, start, longest)
                start = seen[char] + 1
            else:
                longest = max(longest, i - start + 1)
                print("else", i, char, start, longest)
            seen[char] = i

        return longest
    
solution = Solution()
print (solution.lengthOfLongestSubstring("abcdaefghbcbb"))