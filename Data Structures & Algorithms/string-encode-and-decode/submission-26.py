class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for element in strs:
            encodedStr = encodedStr + "#" + str(len(element)) + "#" + element
        return encodedStr
    def decode(self, s: str) -> List[str]:
        strs = []
        countingMode = False
        length = -1
        actualLength = 0
        i = 0
        countNow = False
        print(s)
        areYouSure = False
        for i in range(len(s)):
            if (countNow):
                if not ((s[i]=="#" and i<len(s)-1 and s[i+1].isdigit()) and length == actualLength):   
                    actualLength += 1
            if (countingMode):
                
                if (i+2 < len(s) and s[i+1].isdigit() and s[i+2].isdigit()):
                     length = int(s[i:i+3])
                elif (i+1 < len(s) and s[i+1].isdigit()):
                    length = int(s[i:i+2])
                else:
                    length = int(s[i])
                countingMode = False
                areYouSure = True
            if (s[i] == "#" and areYouSure):
                countNow = True
                areYouSure = False
            if ((s[i]=="#" and i<len(s)-1 and s[i+1].isdigit() and (not areYouSure)) or (i == (len(s)-1))):
                print(length, actualLength)
                if (length == actualLength):
                    print(i)
                    print(length, actualLength)
                    if (i != len(s)-1):
                        strs.append(s[i-length:i])
                    else:
                        strs.append(s[i-length+1:i+1])
                    actualLength = 0
                    length = -1

                if (length == -1):
                    countNow = False
                    countingMode = True
            i += 1

        return strs