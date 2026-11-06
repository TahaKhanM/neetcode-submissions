class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        currentIndex = 0
        stringDictionaries = {}
        finalList = []
        def strToDict(s): 
            myDict = {}
            for c in s:
                if c in myDict:
                    myDict[c] += 1
                else:
                    myDict[c] = 1
            return frozenset(myDict.items())
        for string in strs:
            myDict = strToDict(string)
            print(string, myDict)
            if myDict in stringDictionaries:
                finalList[stringDictionaries[myDict]].append(string)
            else:
                stringDictionaries[myDict] = currentIndex
                finalList.append([])
                finalList[-1].append(string)
                currentIndex += 1
        return finalList