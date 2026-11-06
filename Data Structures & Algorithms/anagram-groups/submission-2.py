class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        currentIndex = 0
        stringDictionaries = {}
        finalList = []
        for string in strs:
            myDict = str(sorted(string))
            if myDict in stringDictionaries:
                finalList[stringDictionaries[myDict]].append(string)
            else:
                stringDictionaries[myDict] = currentIndex
                finalList.append([])
                finalList[-1].append(string)
                currentIndex += 1
        return finalList