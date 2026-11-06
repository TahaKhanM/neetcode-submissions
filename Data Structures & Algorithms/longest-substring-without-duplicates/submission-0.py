class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        partialString = []
        def drop(pS, c):
            while(pS.pop(0) !=  c):
                pass
            return pS
        for i in range(len(s)):
            if (s[i] in partialString):
                partialString = drop(partialString, s[i])
            partialString.append(s[i])
            max_length = max(len(partialString), max_length)
        return max_length