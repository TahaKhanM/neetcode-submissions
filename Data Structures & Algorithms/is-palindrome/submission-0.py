class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(c for c in s if c.isalnum()).lower()
        for i in range(len(string)):
            if (string[i] != string[len(string) - i - 1]):
                return False
        return True
    