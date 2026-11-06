class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestLength = 0
        chrs = {}
        for i in range (len(s)):
            c = s[i]
            if (c in chrs):
                chrs[c][1] += 1
                if i - chrs[c][0] >= k + chrs[c][1]:
                    longestLength = max(longestLength, k + chrs[c][1] - 1)

                    while i - chrs[c][0] >= k + chrs[c][1]:
                        if s[chrs[c][0]] == c:
                            chrs[c][1] -= 1
                        chrs[c][0] += 1
            else:
                chrs[c] = [i, 1]

        for c in chrs:
            longestLength = max(longestLength, k + chrs[c][1])
        return min(longestLength, len(s))