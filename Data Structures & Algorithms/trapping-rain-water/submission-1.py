class Solution:
    def trap(self, height: List[int]) -> int:
        def checkDescending(seq):
            for i in range(1, len(seq)):
                if seq[i] > seq[i -1]:
                    return False
            return True
        x = -1
        total = 0
        added = 0

        unmatchedLargest = [-1, -1]
        i = -1
        for y in height:
            i += 1
            if y >= x:
                x = y
                added = 0
                if (y >= unmatchedLargest[0]):
                    unmatchedLargest[0] = y
                    unmatchedLargest[1] = i
            else:
                total += x - y
                added += x - y
        print(total)
        if (unmatchedLargest[1] != len(height)-1):

            total -= added
            maxLen = len(height) - 1 - unmatchedLargest[1]
            i = -1
            x = -1
            added = 0
            print(unmatchedLargest)
            descending = checkDescending(height[unmatchedLargest[1]:])
            print(height[unmatchedLargest[1]:])
            print(descending)
            if not descending:
                for y in reversed(height):
                    i += 1
                    if (i == maxLen):
                        break
                    if y >= x:
                        x = y
                    else:
                        total += x - y
                        added += x - y
            


        return total