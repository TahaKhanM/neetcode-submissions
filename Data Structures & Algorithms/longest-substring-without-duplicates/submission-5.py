class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        chrs = {}
        for i in range(len(s)):
            if (s[i] in chrs):
               start = max(chrs[s[i]] + 1, start)
            
            chrs[s[i]] = i
            max_length = max(i - start + 1, max_length)

            
        return max_length