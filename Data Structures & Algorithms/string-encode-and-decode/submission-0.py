class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for element in strs:
            encodedStr = encodedStr + element + ";;"
        return encodedStr
    def decode(self, s: str) -> List[str]:
        return s.split(";;")[:-1]