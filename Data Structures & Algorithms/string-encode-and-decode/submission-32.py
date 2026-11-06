class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for element in strs:
            encodedStr = encodedStr + "#" + str(len(element)) + "#" + element
        return encodedStr
    def decode(self, s: str) -> List[str]:
        strs = []
        length = -100
        currentLength = -1
        i = 0
        print(s)
        while( i< len(s)):
            print(i, length, currentLength)
            if((s[i] == "#" and ((currentLength == -1) or (currentLength - 1) == length)) or i == (len(s) - 1)):

                if (i == len(s) - 1): 
                    i += 1
                    currentLength += 1
                if (currentLength-1 == length):
                    if (length != 0):
                        strs.append(s[i-length:i])
                if (i != len(s)):
                    encodedDigit = []
                    j = i + 1
                    while (s[j].isdigit()):
                        encodedDigit.append(s[j])
                        j += 1
                    length = int("".join(encodedDigit))
                    currentLength = 0
                    i += len(encodedDigit) + 1
                    
                if (length == 0):
                    strs.append("")

            currentLength += 1
            i += 1
            
        return strs