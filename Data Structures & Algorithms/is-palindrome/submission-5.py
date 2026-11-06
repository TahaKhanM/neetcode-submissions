class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r and r > 0 and l < len(s):
            while (not (s[r].isalnum())) and r > 0:
                r -= 1

            while (not (s[l].isalnum())) and l < len(s) - 1:
                l += 1

            if (s[l].lower() != s[r].lower()) and (s[l].isalnum()) and (s[l].isalnum()):
                return False
            else:
                l += 1
                r -= 1

        

        return True