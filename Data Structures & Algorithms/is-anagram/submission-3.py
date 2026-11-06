class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def strToDict(s): 
            myDict = {}
            for c in s:
                if c in myDict:
                    myDict[c] += 1
                else:
                    myDict[c] = 1
            return myDict 

        if (strToDict(s) == strToDict(t)):
            return True
        return False
