class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        currentIndex = 0
        stringDictionaries = {}
        finalList = []
        def strToDict(s):
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            return str(chars)
        for string in strs:
            myDict = strToDict(string)
            if myDict in stringDictionaries:
                finalList[stringDictionaries[myDict]].append(string)
            else:
                stringDictionaries[myDict] = currentIndex
                finalList.append([])
                finalList[-1].append(string)
                currentIndex += 1
        return finalList