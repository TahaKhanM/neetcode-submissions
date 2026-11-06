class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = {}
        soFarDict = {}
        for c in s1:
            if c in s1Dict:
                s1Dict[c] +=1
            else:
                s1Dict[c] = 1
        l = 0
        r = 0

        while l <= r and r < len(s2):
            if s1Dict == soFarDict:
                return True
            c = s2[r]
            if c not in s1Dict:
                l = r + 1
                soFarDict = {}
            else:
                if c in soFarDict:
                    soFarDict[c] += 1

                    while not (soFarDict[c] <= s1Dict[c]):
                        c2 = s2[l]
                        if c2 in soFarDict:
                            if soFarDict[c2] > 1:
                                soFarDict[c2] -= 1
                            else:
                                del soFarDict[c2]
                        l += 1  
                else:
                    soFarDict[c] = 1
            r += 1

        if soFarDict == s1Dict:
            return True
        return False